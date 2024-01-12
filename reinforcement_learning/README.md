# Reinforcement Learning

1. link
   * [莫烦PYTHON/reinforcement-learning](https://mofanpy.com/tutorials/machine-learning/reinforcement-learning/)
   * openAI-gym-official-site
   * [github/reinforcement-learning-an-introduction](https://github.com/ShangtongZhang/reinforcement-learning-an-introduction), reproduce results
   * [github/LyWangPX/Reinforcement-Learning-2nd-Edition-by-Sutton-Exercise-Solutions](https://github.com/LyWangPX/Reinforcement-Learning-2nd-Edition-by-Sutton-Exercise-Solutions)
2. package
   * [github/coach](https://github.com/NervanaSystems/coach)
   * [github/tensorforce](https://github.com/tensorforce/tensorforce)
   * [rllib](https://docs.ray.io/en/latest/rllib.html)

## 莫烦PYTHON/reinforcement-learning

1. 应用：alphaGO, atari
2. 方法分类
   * 通过价值选行为：Q learning, Sarsa, Deep Q Network
   * 直接选行为：Polycy Gradients
   * 想象环境并从中学习Model Based RL
   * 不理解环境model-free RL, 理解环境model-based RL
   * 基于概率Policy-Based RL, 基于价值Value-Based RL
   * actor-critic
   * 回合更新Monte-Carlo update，单步更新Temporal-Difference update
   * 在线学习on-policy，离线学习off-policy
3. table lookup Q-learning method: `epsilon-greedy`

## coursera

### week1

1. Martha, Adam, Rich Sutton
2. DQN, Q-learning, Epsilon-greedy action selection
3. multi-arm bandit problem
4. Markov decision process
5. evaluative feedback
6. example: 医生用药、推荐系统，bandit，
7. estimate action values using sample average method
8. greedy action selection
9. exploration-exploitation dilemma
10. incremental update rule: stepsize, target, estimate
11. non-stationary bandit problem
12. epslilon-greedy action selection
13. optimistic initial value
    * only drive early exploration
    * not well-suited for non-stationary problems
    * what the optimistic initial value should be
14. Upper-Confidence Bound (UCB) action selection

John Langford, Microsoft Research, Contextual Bandits for Real World Reinforcement Learning

1. the gap between large simulator and reality
2. temporal credit assignment
3. contextual bandits: epoch greedy (2007)
4. timeline
   * 1995 EXP4 paper
   * 2007 epoch greedy
   * 2010 personalized news
   * 2011 computational and statistics optimized algorithm
   * 2014 better algorithm
   * 2016 created first version of decision service
   * 2019 first RL service product "Azure Cognitive Services Personalizer"
5. tutorial: [github/vowpal-wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)

## week2

1. inverse reinforcement learning
2. meta reinforcement learning
3. evolutionary optimization
4. value function有些像是格林函数？

## week4

1. policy evaluation, control
2. dynamic programing
3. temporal differerent space dynamic，给定dynamic function $p$
4. iterative policy evaluation
5. policy improvement
6. generalized policy iteration
   * value iteration
   * synchronous DP
   * asynchronous DP
7. Monte Carlo Sampling, bootstrapping
8. brute force search

Warren Powell: approximate dynamical programming for Fleet Management

## week5 sample-based learning methods

1. off-policy learning
   * learning from demonstration, parallel learning, facilitating exploration
   * learning an optimal policy from suboptimal behavior
   * target policy, behavior policy
2. importance sampling ratio

Emma Brunskill: batch reinforcemnet learning

1. technique to minimize/understand data needed to learn to make good decision
2. causal reasoning
3. counterfactual reasoning
4. counterfactual/batch policy optimization: learn a good policy that will perform well in the future
5. treatment effect estimation from old data
6. covariate shift: different policies -> different actions -> different state distributions
7. parametric models of dynamics, rewards or values fit to data: low variance, bias
8. importance sampling, correct mismath of state-action distribution: unbiased under certain assuption, high variance
9. doubly robust: (Jiang, Li, 2016), (Thomas, Brunskill, 2016)
10. off-policy gradient with state distribution correction (Liu, Swaminathan, Agarwal, Brunskill, 2019)

## week6 sample-based learning methods

1. temporal difference (TD) learning
2. prediction learning is scalable
3. TD learning is a method for learning to predict

## week7 pass

pass

## week8 model planning

1. Drew Bagnell: self-driving, robotics, model-based RL
   * quadratic value function approximation

## reinforcement learning, an introduction

1. tic-tac-toe
2. optimal control
   * Richard Bellman, the Bellman equation
   * a dynamical system's state, value function
   * Markov decision process: the discrete stochastic version of the optimal control problem
   * dynamic programming
   * policy iteration method
