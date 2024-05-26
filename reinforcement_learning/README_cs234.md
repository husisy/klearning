# CS234

1. link
   * [course-website](https://web.stanford.edu/class/cs234/index.html) lecture slide
   * [youtube-link](https://youtube.com/playlist?list=PLoROMvodv4rOSOPzutgyCTapiGlY2Nd8u) Stanford CS234: Reinforcement Learning

## CS285

Sergey Levine

notation

1. supervisded learning
   * input: $x$
   * output: $y$
   * data: $\left\{ (x_i,y_i) \right\}_{i=1}^N$
   * model: $f(x;\theta)$
   * objective: $\min_{\theta} \sum_{i=1}^N \mathcal{L}(f(x_i;\theta),y_i)$
2. reinforcement learning
   * agent, environment, trajectory
   * state $s_t$
   * observation $o_t$
   * reward $r_t$
   * action $a_t$: discrete or continuous, deterministic or stochastic
   * policy $\pi_\theta(a_t|o_t)$: input $o_t$, output $a_t$
   * transition probality, dynamics $p(s_{t+1}|s_t,a_t)$: input $s_t,a_t$, output $s_{t+1}$
   * data: $\left\{ s_0,a_0,r_0,s_1,a_1,r_1,\cdots,s_T,a_T,r_T \right\}$
   * value function: $V(s)$
   * Q-function: $Q(s,a)$
   * objective: $\max_{\theta} \mathbb{E}_{\tau\sim\pi} \left[ \sum_{t=0}^T \gamma^t r_t \right]$
3. example
   * [arxiv1709.10087](https://arxiv.org/abs/1709.10087) Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
   * [arxiv2304.09834](https://arxiv.org/abs/2304.09834) Learning and Adapting Agility Skills by Transferring Experience
   * [arxiv2209.12827](https://arxiv.org/abs/2209.12827) Advanced Skills by Learning Locomotion and Local Navigation End-to-End
   * [arxiv1312.5602](https://arxiv.org/abs/1312.5602) Playing Atari with Deep Reinforcement Learning
   * [arxiv2305.03270](https://arxiv.org/abs/2305.03270) Deep RL at Scale: Sorting Waste in Office Buildings with a Fleet of Mobile Manipulators
   * [huggingface-link](https://huggingface.co/blog/rlhf) Illustrating Reinforcement Learning from Human Feedback (RLHF)
   * [arxiv2305.13301](https://arxiv.org/abs/2305.13301) training diffusion models with reinforcement learning
4. assumption
   * discrete time
   * Markov decision process

misc

1. link
   * [course-website](https://rail.eecs.berkeley.edu/deeprlcourse/)
   * [youtube-link](https://youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) UC Berkeley CS285: Deep Reinforcement Learning
2. concept
   * RL, reinforcement learning: mathematical formalism for learning-based decision making, approach for learning decision making and control from experience
   * [wiki-link](https://en.wikipedia.org/wiki/Bayesian_network) Bayesian network
3. imitation learning (behavioral cloning): supervised learning from expert demonstrations
   * 1989 ALVINN: autonomous land vehicle in a neural network [wiki-link](https://en.wikipedia.org/wiki/History_of_self-driving_cars#1980s)
   * [arxiv1011.0686](https://arxiv.org/abs/1011.0686) A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning
   * (theoretically) not work: iid assumption in supervised learning
   * (practically) work: data augmentation, domain randomization, adversarial training
   * $O(T^2)$
   * example: [doi-link](https://doi.org/10.1109/LRA.2015.2509024) A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots
   * example: [arxiv1707.02920](https://arxiv.org/abs/1707.02920) Vision-Based Multi-Task Manipulation for Inexpensive Robots Using End-To-End Learning from Demonstration
   * when fail
     * non-Markovian, causal confusion
     * multi-modal: more expressive continuous distribution, discretization with high-dimensional action space
       * mixture of Gaussians, latent variable model, diffusion model
       * autorergressive model
   * example [arxiv2303.04137](https://arxiv.org/abs/2303.04137) Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
4. DAgger: Dataset Aggregation

target

$$ \min_{\theta}E_{a\sim\pi_{\theta}(a\mid s),s'\sim p(s'\mid a,s)}\left[\mathrm{cost}\right] $$

$$ \min_{\theta}E_{s_{1:T},a_{1:T}}\left[\sum_{t}c\left(s_{t},a_{t}\right)\right] $$

$$ p_{\theta}(\tau)=p_{\theta}(s_{1},a_{1},\cdots,s_{T},a_{T})=p(s_{1})\prod_{t=1}^{T}\pi_{\theta}\left(a_{t}\mid s_{t}\right)p\left(s_{t+1}\mid s_{t},a_{t}\right) $$

$$ \theta^{*}=\arg\max_{\theta}E_{\tau\sim p_{\theta}(\tau)}\left[\sum_{t}r(s_{t},a_{t})\right] $$

$$ \theta^{*}=\arg\max_{\theta}\sum_{t=1}^{T}E_{(s_{t},a_{t})\sim p_{\theta}(s_{t},a_{t})}\left[r(s_{t},a_{t})\right] $$

1. Markov chain $M=\{S,T\}$
   * state space $S$
   * transition matrix (operator) $T$
2. Markov decision process $MDP=\{S,A,T,r\}$
   * action space $A$
   * reward function $r: S\times A\to \mathbb{R}$
3. partially observable Markov decision process $POMDP=\{S,A,T,r,O,\Omega\}$
   * observation space $O$
   * observation function (emission probablity) $\Omega: S\to O$
4. stationary distribution $\mu$: always exists under some regularity conditions
5. anatomy of RL
   * generate samples (run policy in environment)
   * fit a model, estimate the return
   * improve the policy
6. types of RL algorithms
   * policy gradient: directly differentiate the objective
   * value based: estimate value function or Q-function of the optimal policy (no explicit policy)
   * actor-critic: estimate value function or Q-function of the current policy
   * model-based: estimate the transition model, and then
     * use it for planning (no explicit policy)
     * use it to improve the policy
     * something else
7. tradeoff between RL algorithms
   * sample efficiency
   * stability, ease of use
   * different assumption
     * stochastic or deterministic
     * continuous or discrete
     * episodic or infinite horizon
8. off-policy and on-policy
   * off-policy: learn from data generated by a different policy
   * on-policy: learn from data generated by the current policy
   * spectrum (most efficient to least efficient)
     * evolutionary or gradient-free RL
     * on-policy policy gradient RL
     * actor-critic style RL
     * off-policy Q-learning
     * model-based deep RL
     * model-based shallow RL
9. finite horizon case, infinite horizon case

algorithm

1. value function fitting methods
   * Q-learning, DQN
   * temperal difference learning
   * fitted value iteration
2. policy gradient methods
   * REINFORCE
   * natrual policy gradient
   * trust region policy optimization
3. actor-critic methods
   * DDPG
   * PPO
   * A3C: asynchronous advantage actor-critic
   * SAC: soft actor-critic
4. model-based methods
   * Dyna
   * Guided policy search

## HuggingFace Deep RL course

misc

1. link
   * [github/CleanRL](https://docs.cleanrl.dev/)
   * [huggingface-link](https://huggingface.co/learn/deep-rl-course/en/unit0/introduction)
