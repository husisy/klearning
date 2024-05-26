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

## misc00

强化学习

定义：

1. Markovian process: state `s`, action `a`, reward `r`, sequence `s0,a0,r1,s1,a1,r2,s2,a2,r3,...`
   * environment由state描述，environment给出reward
   * agent采取action，agent“最大化reward”
2. environment dynamic `p(r',s'|s,a)`: 给定当前状态s和动作a，环境给出奖励r以及跳转至状态`s'`的概率。environment dynamic完全由当前状态和动作决定（markov假设）
3. policy `pi(a|s)`：agent在状态s下时采取动作a的概率
   * deterministic policy
   * stochastic policy
4. 优化目标return
   * 一定会终止的任务episodic task：summation of reward
   * 不会终止的任务continuing task: discounted summation of reward
   * 不会终止的任务continuing task：differential return。average reward，在策略pi下状态s出现的概率，状态s下按照策略pi获得reward的均值，确保这个求和不会发散，average reward也需要在算法中估计出来
5. value function
   * state value function `v_pi(s)`: 从状态s出发，按照策略pi的return期望
   * action value function `q_pi(s,a)`：在状态s选择动作a，然后按照策略pi的return期望
   * 两者可以相互转化
   * 对于differential return需使用Cesàro summation极限下的收敛
6. Bellman期望方程，Bellman最优方程，policy improvement theorem
   * 前者是线性方程，后者是非线性方程，后者的解也满足前者的解（最优策略满足一般策略）
   * given two policy `pi1` and `pi2`, if for all state `s`, `q_pi1(s,pi2(s))>=v_pi1(s)`, then `v_pi2>=v_pi1`
   * 偏序关系`pi>=pi' if v_pi(s)>=v_{pi'}(s) for all s`
   * 最优policy的state value function一定比大于等于其他policy
   * 最优解一定存在但可能不唯一，最优解可以是stochastic policy（方格点迷宫问题）
   * Markovian过程的最优解一定是deterministic policy，non-Markovian过程的最优解可以不是deterministic policy（例如Short corridor with switched actions）
7. 找最优策略
   * 一个直接的想法：直接自洽求解非线性Bellman最优方程：例如动态规划算法dynamic programming，计算量不可接受，信息不完备时不可操作，Broyden算法应该也属于这一类
   * Generalized Policy Iteration (GPI)：从任意一个策略pi出发，求解该策略对应的value function，由该value function导出更优策略`pi'(s)=argmax(q(s,a))`（由policy improvement theorem保证），迭代该过程直至策略收敛
   * GPI：dynamic programming, monte carlo method, TD, Q-learning, Sarsa, actor-critic
   * 思考：在RL中一个非线性方程的自洽求解可以转化为一系列的算法，这些算法能否用于求解物理领域的非线性方程
   * 接下来主要考虑离散可数的状态集以及离散可数的动作集，连续的状态集需要「将value function用函数拟合来替代」，连续的动作集需要「将policy用函数拟合来替代」
8. 动态规划dynamic programming
   * predict任务指给定policy估计value function，control任务指寻找最优policy
   * policy evaluation (predict): Bellman期望方程迭代至收敛
   * policy iteration (control)：Bellman期望方程迭代至收敛，然后更新一次策略，循环直至收敛
   * value iteration (control)：Bellman最优方程迭代至收敛 (fig)
   * 主要用于理论分析，需要假定已知environment dynamic
9. Monte Carlo methods
   * predict: 给定策略下产生尽可能多的sequence `s0,a0,r1,s1,a1,r2,s2,a2,r3,...`，计算sequence每个时刻`(S_t,A_t)`的return，然后取平均作为`q(s,a)`的估计
   * control：在predict基础上，每个episodic之后，更新策略`pi(s)=argmax_a(q(s,a))`
   * control中存在的问题，`(s,a)`可能一次都没有出现
   * Exploring starts（sequence的起始点随机选取保证每个组合都至少出现一次）
   * epsilon-soft policy (fig)：每个action至少有非零概率被抽中，最终训练得到的是近似最优policy
   * off-policy：分为target policy与behavior policy，使用behavior policy产生sequence，target policy来更新value function，两者的return相差系数可用importance sampling确定
   * 特点：不需要environment dynamic（称作model-free method），必须是epoisodic task，必须等到episodic结束才能开始计算（不适用于online learning）
10. Temporal Difference (TD) Learning
    * TD error
    * predict (fig)：formula 获得下一状态和奖励时来更新上一状态
    * SARSA (control): 在predict的基础上，更新完之后使用新的value function来更新策略
    * Q-Learning (control)
    * Expected SARSA (control)
    * 特点：model-free method, online，收敛快
11. 连续的状态集合：将value function用函数拟合来替代
    * 引入记号
    * 选用mean square loss
    * Gradient Monte Carlo method
    * Semi-Gradient SARSA eq10.2
12. 连续的动作集合：「将policy用函数拟合来替代」
    * `pi(a|s,theta)`
    * average reward对于theta的导数等于xxx的期望（证明过程未完全看懂）
13. 区别于监督学习
    * reward不可导
14. 个人局限性：大概只了解到最朴素的RL方法，更前沿的RL方法可以留到具体的科研任务来学习

方法

1. 动态规划
2. Monte Carlo
3. planning
4. SARSA and Q-learning
5. actor-critic

例子

1. k-armed bandit problem：k个赌博机，每个赌博机每次按照内禀分布给出reward，目标最大化average reward。无状态集，action集合为「k个赌博机中选一个」，continuing
2. Short corridor with switched actions P323：自最左边格点出发，抵达最右边格点结束，每一步reward=-1，第二个格点的状态改变与动作相反
   * 状态可区分：最优解显而易见
   * 状态不可区分：agent不被告知处于第几个格点，此时模型不再满足markov模型（环境状态改变与历史动作相关），最优策略是以`2-sqrt(2)`向右移动
3. 平衡杆P56，状态集合包含偏转角/角速度/小车速度/小车坐标，动作集合包含小车加速度，平衡杆偏角过大或者小车越出边界即介绍，目标是最大化竖直平衡杆，视作episodic/continuing任务皆可，每一步获得reward=1制作结束，或者每一步reward=0知道结束获得reward=-1。此问题中，状态集可以是离散的也可以是连续的，动作集也可以是离散或者连续的
4. 方格点行走P76：状态集是格点所在位置，动作集是上/下/左/右（如果动作碰撞到边界则保持在），最左上和最右下格点为终止格点，每一步reward=-1，最优解不唯一
5. 赌徒问题P84：状态集
6. blackjack P93
7. racetrack P111: 赛车从起点出发，向重点前进
8. 转圈圈问题
9. random walk P125: 从中间开始，抵达两端即结束，左端reward=0，右端reward=1，其余reward=0。状态集为格点位置，动作集为左/右，对于随机策略，state value function易解为`{1,2,3,4,5}/6`
10. Windy Gridworld P130：agent自S点开始移动，直至移动到G点结束，每一步reward=-1，每一列下方的数字a代表风强度，即下一状态会多向上偏移a个单位，状态集是agent坐标，动作集是上/下/左/右，图中蓝线是SARSA找到的最优策略
11. mountain car P245
