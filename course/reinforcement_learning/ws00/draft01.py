import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
plt.ion()

# https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html
class BernoulliBandit:

    def __init__(self, n, probas=None):
        self.n = n
        if probas is None:
            probas = np.random.rand(n)
        self.probas = probas
        self.best_proba = self.probas.max()

    def generate_reward(self, i):
        if np.random.random() < self.probas[i]:
            return 1
        else:
            return 0

class Solver:
    def __init__(self, bandit):
        self.bandit = bandit
        self.counts = np.zeros(self.bandit.n, dtype=np.int)
        self.actions = []  # A list of machine ids, 0 to bandit.n-1.
        self.regret = 0
        self.regrets = []  # History of cumulative regret.

    @property
    def estimated_probas(self):
        raise NotImplementedError

    def run_one_step(self):
        raise NotImplementedError

    def run(self, num_steps):
        for _ in range(num_steps):
            i = self.run_one_step()
            self.counts[i] += 1
            self.actions.append(i)
            self.regrets.append(self.bandit.best_proba - self.bandit.probas[i])


class EpsilonGreedy(Solver):
    def __init__(self, bandit, eps, init_proba=1.0):
        """
        eps (float): the probability to explore at each time step.
        init_proba (float): default to be 1.0; optimistic initialization
        """
        super(EpsilonGreedy, self).__init__(bandit)
        self.eps = eps
        self.estimates = np.ones(self.bandit.n, dtype=np.float)*init_proba

    @property
    def estimated_probas(self):
        return self.estimates

    def run_one_step(self):
        if np.random.rand() < self.eps:
            i = np.random.randint(0, self.bandit.n)
        else:
            i = np.argmax(self.estimates)
        r = self.bandit.generate_reward(i)
        self.estimates[i] += (r - self.estimates[i]) / (self.counts[i] + 1)
        return i


class UCB1(Solver):
    # upper confidence bounds
    def __init__(self, bandit, init_proba=1.0):
        super(UCB1, self).__init__(bandit)
        self.t = 0
        self.estimates = np.ones(self.bandit.n, dtype=np.float)*init_proba

    @property
    def estimated_probas(self):
        return self.estimates

    def run_one_step(self):
        self.t += 1
        i = np.argmax(self.estimates + np.sqrt(2*np.log(self.t)/(1+self.counts)))
        r = self.bandit.generate_reward(i)
        self.estimates[i] += (r - self.estimates[i]) / (self.counts[i] + 1)
        return i


class BayesianUCB(Solver):
    """Assuming Beta prior."""

    def __init__(self, bandit, c=3, init_a=1, init_b=1):
        """
        c (float): how many standard dev to consider as upper confidence bound.
        init_a (int): initial value of a in Beta(a, b).
        init_b (int): initial value of b in Beta(a, b).
        """
        super(BayesianUCB, self).__init__(bandit)
        self.c = c
        # Gaussian posterior
        self.as_ = np.ones(self.bandit.n, dtype=np.int)*init_a
        self.bs = np.ones(self.bandit.n, dtype=np.int)*init_b

    @property
    def estimated_probas(self):
        return self.as_ / (self.as_ + self.bs)

    def run_one_step(self):
        i = np.argmax(self.as_/(self.as_+self.bs) + self.c*scipy.stats.beta.std(self.as_,self.bs))
        r = self.bandit.generate_reward(i)
        self.as_[i] += r
        self.bs[i] += (1 - r)
        return i


class ThompsonSampling(Solver):
    def __init__(self, bandit, init_a=1, init_b=1):
        """
        init_a (int): initial value of a in Beta(a, b).
        init_b (int): initial value of b in Beta(a, b).
        """
        super(ThompsonSampling, self).__init__(bandit)
        self.as_ = np.ones(self.bandit.n, dtype=np.int)*init_a
        self.bs = np.ones(self.bandit.n, dtype=np.int)*init_b

    @property
    def estimated_probas(self):
        return self.as_ / (self.as_ + self.bs)

    def run_one_step(self):
        i = np.argmax(np.random.beta(self.as_, self.bs))
        r = self.bandit.generate_reward(i)
        self.as_[i] += r
        self.bs[i] += (1 - r)
        return i


if __name__ == '__main__':
    num_slot_machine = 10
    num_step = 5000
    bandit = BernoulliBandit(num_slot_machine)
    solvers = [
        # (EpsilonGreedy(bandit, 0), 'Full-exploitation'),
        # (EpsilonGreedy(bandit, 1), 'Full-exploration'),
        (EpsilonGreedy(bandit, 0.01), r'$\epsilon$-Greedy'),
        (UCB1(bandit), 'UCB1'),
        (BayesianUCB(bandit, 3, 1, 1), 'Bayesian UCB'),
        (ThompsonSampling(bandit, 1, 1), 'Thompson Sampling'),
    ]

    for x,_ in solvers:
        x.run(num_step)

    fig,(ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(12,4))

    for x,y in solvers:
        ax1.plot(range(len(x.regrets)), np.cumsum(np.array(x.regrets)), label=y)
    ax1.set_xlabel('Time step')
    ax1.set_ylabel('Cumulative regret')
    ax1.legend()
    ax1.grid('k', ls='--', alpha=0.3)

    # Sub.fig. 2: Probabilities estimated by solvers.
    xdata = np.arange(num_slot_machine)
    sorted_indices = np.argsort(bandit.probas)
    ax2.plot(xdata, bandit.probas[sorted_indices], 'k--', markersize=12)
    for s,_ in solvers:
        ax2.plot(xdata, s.estimated_probas[sorted_indices], 'x', markeredgewidth=2)
    ax2.set_xlabel('Actions sorted by ' + r'$\theta$')
    ax2.set_ylabel('Estimated')
    ax2.grid('k', ls='--', alpha=0.3)

    # Sub.fig. 3: Action counts
    xdata = np.arange(num_slot_machine)
    sorted_indices = np.argsort(bandit.probas)
    ax3.plot(xdata, bandit.probas[sorted_indices], 'k--', markersize=12)
    for s,_ in solvers:
        ax3.plot(xdata, s.counts[sorted_indices]/num_step, 'x', lw=2, markeredgewidth=2)
    ax3.set_xlabel('Actions')
    ax3.set_ylabel('Frac. # trials')
    ax3.grid('k', ls='--', alpha=0.3)
