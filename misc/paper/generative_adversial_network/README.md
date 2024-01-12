# GAN

TODO-read

TODO-add arxiv-link

1. GAN-Goodfellow, arxiv-1406
2. reconstruction object function, 10-1007-ref13/ref8/ref143/ref147x
3. PSGAN-paper
4. latent space decomposition
5. conditional GAN (CGAN) 10-1007-ref80
6. BiGAN, adversiarially learned inference (ALI)
7. variational autoencoder
8. Laplacian pyramid of adersarial networks (LAPGAN)
9. unsupervised representation learning with deep comvolutional generative adversarial networks, arxiv2015, 10-1007-ref13, 必须看，与那篇matGAN相关
10. LSUN dataset
11. adversarial autoencoders, Goodfellow, arxiv2015, 10-1007-ref75
12. generative recurrent adversarial networks (GRAN)
13. Information maximizing generative adversiarial networks (InfoGAN)
14. Bidirectional Generative Adverserrial Networks (BiGAN)
15. [pytorch-GAN-zoo](https://github.com/facebookresearch/pytorch_GAN_zoo)
16. visual Turing test
17. Wasserstein GAN (WGAN) 必须看 10-1007-ref4/ref37
18. variational auto-encoder (VAE)
19. 二阶优化也许有帮助收敛问题
20. arxiv1511.01844：非监督学习评估方式，见dcgan
21. arxiv1509.01240: a direct link between how fast models learn and their generalization performance，与二阶优化器相关

## Vanilla GAN

1. 想解决的问题：给定一些样本数据`{x1,x2,...,xn}`，生成更多相似但不同的数据
2. 使用一个单变量示例
   * （上帝知道）样本数据产生自高斯分布`x~N(mu0,sigma0)`
   * 生成器generator输入正态分布随机噪音`z~N(0,1)`，输出假数据`G(z)=w0z+b0`
   * 判别器discriminator输入数据，输出其是真样本的概率`D(x)=sigmoid(w1*x+b1)`
   * 前向过程：计算假数据的概率`D(G(z))`和真数据的概率`D(x)`
   * 反向过程1：用`-log(D(x))-log(1-D(G(z)))`作为loss计算`w1/b1`的梯度并更新discriminator，即cross-entropy
   * 反向过程2：用`-log(D(G(z)))`作为loss计算`w0/b0`的梯度并更新generator
   * 预期收敛结果：`(w0,b0)`收敛至`(sigma0,mu0)`附近。对于这么一个过于简单的模型似乎只有`b0`可以收敛但`w0`应该不会收敛
   * 生成新数据：假设收敛，从而`G(z)`即满足上帝知道的数据分布，
   * GAN论文中提及的min-max loss，上述例子中`min_G`与公式不一致（似乎是论文中这个公式极易造成训练发散）
3. 极大极小算法
   * [link](https://www.zhihu.com/question/27221568)
   * 与GAN相关，很相似，但不太说的上两者的联系，似乎可以加深理解
   * 井字棋游戏：`3x3`网格，双方交替下棋，三个子连成线为赢。可以用树状图枚举所有情形，每一行代表其中一方下棋，并且将赢/平/输打分`1/0/-1`
   * 类似的，假设有右图这样的树状图，并且为所有最终情况打好分，对手下棋会最小化分数，己方下棋会最大化分数，由此可以倒退倒数一步的选择，依次递推可以得到最优选择路径及其分数-7
4. 解释这个minmax loss函数，零和游戏/纳什均衡/博弈论，极大极小算法
5. 在神经网络中的更新策略

## conditional GAN

1. 想解决的问题：给定一些带标签的样本数据`{(x1,y1),(x2,y2),...,(xn,yn)}`，生成更多指定标签下相似但不同的数据
2. mnist数字0-9识别数据集
   * 目标：生成特定标签y（数字0-9）的生成图片
   * generator同时输入正态分布随机变量`z~N(0,1)`和标签`y`，输出`(28,28)`大小矩阵的假数据，`z`一般是矢量即高维独立正态分布，标签`y`可以使用one-hot矢量或者词嵌入矢量，然后与`z` concatenate到一块然后输入到`dense/conv`神经网络中
   * discriminator输入真图片与标签`(x,y)`预测概率，输入假图片与标签`(G(y,z),y)`预测概率
   * 其余与GAN相同
   * 生成的fake-image与real-image送给discriminator计算给定标签下的softmax cross-entropy loss（或者是联合分布下的预测真假） *TODO确认代码实现*，个人预期两种都可行，原文使用的应该是联合分布下的预测真假
   * generator/discriminator中使用dropout
3. multimodal, YFCC100M数据集
   * 目标：为图片打标签
   * generator输入随机变量与图片特征`(z,imagevec)`，输出一个词向量`fake-wordvec`，图片特征通过Imagenet数据集上预训练的网络提取
   * discriminator输入图片向量和真实词向量`(imagevec,real-wordvec)`预测概率，输入图片向量与假词向量`(imagevec,fake-wordvec)`预测概率，真实标签的词向量通过YFCC100M上预训练skip-gram模型获得
   * 其余与GAN相同
   * 然后便可以输入一幅图，使用100个随机向量，生成最接近的词向量

## variational autoencoder VAE

[知乎link](https://zhuanlan.zhihu.com/p/34998569)

1. 统一约定：`x`表示数据（例如mnist中的图片），`y`表示标签，`z`表示latent space（嵌入向量/特征向量/隐变量）
2. 理论没有太看懂
   * 一些专业术语：prior `p(z)`, posterior `p(z|x)`, likelihood `p(x|z)`
   * 理论似乎是对应于general distribution的prior `p(z)`，下面这个例子使用正态分布为例
   * 作用：generate artirficial data, encode data
   * Stochastic Gradient Variational Bayesian (SGVB)
   * KL-divergence loss + reconstruction error（见eq1）
3. auto-encoder
   * 最小化reconstruction error
   * encode the data into latent space
   * decoder不能作为generator来生成相似的数据
4. mnist例子
   * encoder：输入mnist图片，输出`2n`个数，前`n`个称作平均值`mu`，后`n`个称作标准差`sigma`
   * decoder：输入高斯分布随机变量`z~N(mu,sigma)`，输出mnist长宽的图片，计算KL-divergence以及reconstruction loss（见eq2）
   * reparameterization trick: 从`N(mu, sigma)`中采样一个`z`，等价于从`N(0,1)`中采样`epsilon`，然后令`z = sigma*epsilon + mu`，前者是没法梯度方向传播但后者可以
   * reconstruction error会使网络逼近`sigma=0`的自编码器
   * KL-divergence为`N(mu,sigma)`分布相对`N(0,1)`分布，KL-divergence会使网络逼近`sigma=1, mu=0`
   * 生成新数据：随机变量`z~N(0,1)`作为decoder的输入即可
   * 论文中理论似乎是给出了general prior distribution的推导，该例子只展示了正态分布
5. manifold visualization：使用2d latent space进行训练，然后选取CDF等距离网格点生成新数据
6. 与之前的文章，在likelihood lower bound/marginal likelihood方面进行了对比

## Adversarial Autoencoder AAE

1. mnist例子
   * 三部分组成：encoder，decoder，discriminator
   * encoder/decoder与自编码器一致
   * encoder输入图片，输出latent space即压缩向量
   * latent space与随机变量（例如正态分布）输入到discriminator进行对抗训练，随机变量也可以是其它分布
   * 生成新数据：随机变量作为decoder的输入即可
   * 结论1：fig-A与fig-C对比，the coding space has holes for VAE which means VAE may not have captured the data manifold as AAE
   * 结论2：fig-B与fig-D对比，随机变量（prior distribution）选取为10 2d Gaussian， the AAE successfully matched the aggregated posterior with prior distribution

## Deep Convolutional Generative Adversarial Netoworks DCGAN

1. contribution
   * 提出了一系列建议使得更深更大的GAN模型训练稳定
   * ImageNet上训练DCGAN（非监督学习），用discriminator对cifar10训练集提取特征，用cifar10训练集的特征训练SVM进行分类（监督学习），在cifar10验证集上评估。competitive performance，略差于`ExemplarCNN`
   * 训练后的GAN filter能够“操作”特定的目标（未看懂）
   * 矢量运算vector arithmetic property
2. unsupervised representation learning: K-means, hierarchical clustering of image patchs, autoencoder, ladder structure, separating the what and where components of the code
3. 已有的generative image models
   * VAE: blurry
   * iterative forward diffusion process (arxiv1503.03585)
   * GAN: noisy, incomprehensible
   * laplacian pyramid GAN (arxiv1506.05751): wobbly
4. 使DCGAN训练稳定的技巧
   * 将`pooling`替换为`conv/deconv`
   * 使用`batchnormlization`，除去generator输出层，BN一定程度上能够防止generator collapsing all samples to a single point
   * 尽可能不用fully connected hidden layer，除去generator第一层和discriminator最后一层（只能使用fc-layer），global average pooling increase model stability but hurt convergence speed
   * generator中使用`relu`，generator最后一层使用`tanh`（使输出在`[-1,1]`范围内），discriminator使用`leaky_relu`
   * Adam优化器`beta1=0.5`会比`beta1=0.9(default)`稳定
5. 论述generator不是在overfit/memorize training samples：当使用小学习率，如果在一个epoch结束时能够产生较好的图片则说明不是记住了训练数据，no prior empirical evidence demonstrating memorization with SGD and a small learning rate
6. 照片去重：autoencoder， binaried thresholding, semantic-hashing (arxiv1410.1165)，减少训练数据中的重复数据，避免generator记住了训练数据
7. 收集人脸数据：在dbpedia收集10000个人名，用这些人名在网上搜索照片，然后使用opencv提取人脸部分
8. （ImageNet）非监督学习DCGAN作为特征提取器，会比相同的网络结构只在cifar10上训练最终在cifar10验证集上评估的分数高：大数据集的泛化能力强
9. arxiv1511.01844
   * nearest neighbors in pixels or feature space are trivially fooled by small image transforms
   * log-likelihood metric is a pool metric to quantitatively assess the model
10. 评估GAN
    * latent space线性插值：a sharp transition is the sign of memorization。能够看出how the space is hierarchically collapsed
    * discriminator feature: 特征对于输入图片求导找最重要的部分 guided backpropagation (arxiv1412.6806)，heatmap
    * generator feature（未理解）：对训练后的dcgan引入一些「是否有窗的数据」进行finetune，进而生成有窗/无窗的图片
    * latent space矢量运算：man with glasses - man without glasses + woman without glasses = woman with glasses
    * latent space矢量运算：man looking right + turn vector = man looking left

## Wasserstein GAN WGAN

1. contribution
   * （没看懂）理论分析了Earth Mover (EM) distance比Total Variation(TV) distance, Kullback-Leibler (KL) divergence, Jensen-Shannon (JS) divergence好在learning distribution方面
   * WGAN使用EM distance
   * WGAN训练稳定，loss有意义，避免了mode dropping phenomenon
2. 算法流程见文章，相比GAN的区别
   * GAN包含generator与discriminator，WGAN包含generator与critic（换个名字）
   * WGAN的critic需要将可训练参数强行限定上下界：文中也表示weight clipping is a clearly terrible way to enfore a Lipschitz constraint
   * critic更新多步，generator才更新一步：the better the critic, the higher quality the gradients we use to train the generator。但对于GAN，as the discriminator gets better the gradients get more reliable but the true gradient is 0.
   * loss计算几乎相当于：把discriminator最后一步输出的非线性激活函数sigmoid去掉了
3. WGAN带来的好处
   * loss metric指示了generator的收敛程度以及生成图片质量，但不作为定量评估图片质量的指标
   * 训练稳定：即使不使用DCGAN中的建议，例如去掉BN也能收敛
   * 避免了mode dropping phenomenon：the optimal generator for a fixed discriminator is a sum of deltas on the points the discriminator assigns the highest values
4. WGAN：momentum-based optimizer多半不收敛
   * the loss for the critic is nonstationary, RMSProp is known to perform well on very nonstationary problems (arxiv1602.01783, reinforcement learning)
   * we identified momentum as a potential cause: as the loss blew up, the cosine between the adam step and the gradient usually turned negative

## metric

一些传统的评估方法

1. likelihood estimated by annealed importance sampling, depends on the noise assumptions for the real data and can be dominated by single sample
2. density estimates
3. loss：不同GAN的loss function差异巨大

### inception score

1. a note on the inception score, [arxiv](https://arxiv.org/abs/1801.01973)
2. 一些常见的评估方法: inception score, mode score, Frechet Inception distance
   * 值得注意的是：these scores are often motivated by demonstrating that it prefers models that generate realistic and varied images and is correlated with visual quality
3. `IS(g)`公式见下，以下一律加上对数运算`ln(IS(g))`
   * `ln(IS(g))`越大越好
   * by removing the exponential which the original authors includded only for aesthetic purposes
   * `ln(IS(g))=I(y;x)`就是mutual information
   * `ln(IS(g))=H(y)-H(y|x)`和entropy的关系：generator需要产生清晰的图片，换言之在inception-v3模型的预测中需要给出非常高的预测概率，等价于`p(y|x)`的熵尽可能小。另一方面，generator需要diversity而避免mode collapse，也就是说`p(y)`的熵需要尽可能大（尽可能接近均匀分布）
   * `0<=ln(IS(g))<=ln(1000)`
   * 数值计算时建议：每次生成`5000`张图来计算inception score，计算`10`次，然后取均值
4. inception score存在的问题
   * 对于inception-v3模型的参数敏感，每次随机初始化获得的模型不一样，之后计算的inception score也会差异较大
   * 数值计算需要多次取样平均，对于ImageNet-val数据集只有50000张图不太方便，对于GAN可以产生任意张图还可以接受
   * inception-v3只在ImageNet数据集上训练，不适用于其它数据集（目前GAN社区大多数实验是在cifar10上进行的），预测的分类和cifar10本身的分类很不匹配
   * 用inception score来进行超参数调优会给出错误的优化方向（产生很不真实图片的生成器但inception score很高）
   * 无法评估过拟合：把部分训练集记忆下来的生成器的inception score也能很高，极端情况是「仅生成1000张非常真实的图，每张图对应一个分类」

$$
IS\left( g \right) =\exp \left( \mathbb{E}_{x\sim p_g}D_{KL}\left( p\left( y|x \right) \parallel p\left( y \right) \right) \right)
$$

### Frechet Inception Distance

首次提出FID: GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium, [arxiv](https://arxiv.org/abs/1706.08500)

1. 主要是为了解决：inception score未使用real data
2. 使用inception-v3提取倒数一层的特征：`2048`维度的向量
   * 假设这`2048`维度的向量是一个多维高斯分布：mean and covariance
   * 计算real data和fake data对应的多维高斯分布的mean和covariance
   * 由mean和covariance计算Frechet distance
   * 使用其它层数也可以
   * FID越小越好
3. 在CelebA数据集上，添加各种噪声，分别计算FID/IS与噪声强度的关系
   * `IND = m - IS`
   * inception score在这几个测试上表现糟糕
   * 对于WGAN-GP训练过程中，专门拧出几个阶段来看，FID与quality是一致的（未对比IS）

分析FID：Are GANs Created Equal? A Large-Scale Study, [arxiv](https://arxiv.org/abs/1711.10337)

1. FID无法评估过拟合
2. FID high bias and low variance
3. FID对于mode dropping敏感：mode dropping约严重，FID约高
4. discussing the best score obtained by a model on a data set is not a meaningful way to discern between these models. One should instead discuss the distribution of the obtained scores.
