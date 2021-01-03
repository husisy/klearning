# Generative Adversarial Networks

[this-person-does-not-exist](https://thispersondoesnotexist.com/)

[this-cat-does-not-exist](https://thiscatdoesnotexist.com/)

## week1 intro to GANs

1. 记号约定：feature `X`, class `Y`
2. discriminative model: classifier, `P(Y|X)`, distinguish between classes
3. generative model `P(X)`或者`P(X|Y)`, learn to produce realistic examples
   * random noise是必要的，a model generating only one dogy is pointless
4. 常见生成模型
   * Variational Autoencoder (VAE)
   * Generative Adversarial Network (GAN)
5. application
   * styleGAN2, [github](https://github.com/NVlabs/stylegan2), [arxiv](https://arxiv.org/abs/1912.04958)
   * CycleGAN
   * GauGAN
   * Few-shot adversarial learning of realistic neural talking head models, [arxiv](https://arxiv.org/abs/1905.08233)
   * 3D-GAN, generative design
6. binary crosss entropy (BCE)
7. GAN train in an alternating fashion, two models should always be at a similar skill level
8. noise vector
   * 100 iss standard, some researchers might use a power of 2,
   * truncation trick
9. discriminator use leaky ReLU to prevent the "dying ReLU" problem
10. reading material
    * Hyperspherical Variational Auto-Encoders, S-VAE, [arxiv](https://arxiv.org/abs/1804.00891)
    * Analyzing and Improving the Image Quality of StyleGAN, [arxiv](https://arxiv.org/abs/1912.04958)
    * Semantic Image Synthesis with Spatially-Adaptive Normalization, [arxiv](https://arxiv.org/abs/1903.07291)
    * Few-shot Adversarial Learning of Realistic Neural Talking Head Models, [arxiv](https://arxiv.org/abs/1905.08233)
    * Learning a Probabilistic Latent Space of Object Shapes via 3D Generative-Adversarial Modeling, [arxiv](https://arxiv.org/abs/1610.07584)
    * these cats do not exist, [website](https://thesecatsdonotexist.com/)

## week2 deep convolutional GANs

1. activation function: `relu`, `leaky_relu`, `sigmoid`, `tanh`
   * `relu`: "dying ReLU" problem
   * `sigmoid`: vanishing gradient and saturation problems
   * `tanh`: keeps the sign of the input, vanishing gradient and saturation problems
2. batch normalization: reduce the internal covariate shift, stablize the GAN training
3. convolution, padding, stride, pooling, upsampling, transposed convolutions
   * transposed convolution: checkerboard pattern issue, replaced by "upsampling + convolution"
4. checkerboard pattern issue, [link](https://distill.pub/2016/deconv-checkerboard/)
   * use a kernel size that is divided by your stride, avoiding the overlap issue
5. dcgan
   * do NOT use pooling layer
   * use batch normalization in both the generator and the discriminator
   * dot NOT use fully-connected hidden layer
   * use relu in generator
   * use leaky-relu in discriminator

## week3 Wasserstein GANs with Gradient Penalty

1. modes are peaks in the distribution of features
2. mode collapse happens when the generator gets stuck in one mode
3. BCE loss are susceptible to vaishing gradient problems
   * when the discriminator improves too much, the function approximated by BCE loss will contain flat regions on the cost function (vanishing gradients)
   * `min max -E(log(d(x))) + E(1-log(d(g(z))))`
4. Earth Mover's Distance (EMD)
   * effort to make the generated distribution equal to the real distribution
   * doesn't have flat regions when the distributions are very different
   * approximating EMB solves the problems associated with BCE
   * `min max E(c(x)) - E(c(g(z)))`
   * critic
   * 1-Lipschitz continuous: the norm of th e gradient should be at most 1 for every point, ensure that W-Loss is validly approximating Earth Mover's Distance
   * weight clipping: limits the learning ability of the critic
   * gradient penalty, regularization: work better
5. spectrally norm
   * Spectral Norm Regularization for Improving the Generalizability of Deep Learning, [arxiv](https://arxiv.org/abs/1705.10941)
   * Spectral Normalization for Generative Adversarial Networks, SNGAN, [arxiv](https://arxiv.org/abs/1802.05957)
6. reading material
   * From GAN to WGAN, [lil's-log](https://lilianweng.github.io/lil-log/2017/08/20/from-GAN-to-WGAN.html), [arxiv](https://arxiv.org/abs/1904.08994)
   * Improved Training of Wasserstein GANs, [arxiv](https://arxiv.org/abs/1704.00028)

## week4 conditional GAN, controllable generation

1. conditional generation
   * require labeled datasets
   * examples can be generated fro the selected class
2. generator: noise vector and class vector (usually one-hot)
3. discriminator: the class is passed to the discriminator as one-hot matrices
4. controllable generation vs conditional generation
   * example with the features that you want, examples from the classes you want
   * training dataset doesn't need to be labeled, training dataset needs to be labeled
   * manipulate the z-vector input, append a class vector to the input
5. controllable generation
   * the goal is to find these directions for different features you care about
   * to control ouput features, you need to find directions in the z-space
   * to modify your output, you move around in the z-space
6. challenges with controllable generation
   * when trying to control one feature, others that are correlated change
   * z-space entanglement makes controllability difficult, if not impossible
   * entanglement happens when z does not have enough dimensions
7. classifier gradients
   * modify just the noise vector until the feature emerges
   * classifiers can be used to find directions in the z-space
   * to find directions, the updates are done just to the noise vector
8. disentanglement
   * latent factors of variation
   * disentangled z-space let you control individual features by corresponding z-values directly to them
   * there are supervised (difficumlt for continuous classes) and unsuperviced (add regularization) methods to achieve disentanglement
9. reading material
   * Conditional Generative Adversarial Nets, [arxiv](https://arxiv.org/abs/1411.1784)
   * Interpreting the Latent Space of GANs for Semantic Face Editing, InterFaceGAN, [arxiv](https://arxiv.org/abs/1907.10786)

## week5 evaluation of GANs

1. challenging to evaluate: no ground truth
2. fidelity measures image quality and diversity measures variety
3. evaluation metrics try to quantify fidelity and diversity
4. pixel distance is simple but unreliable, feature distance uses the higher level features of an image, making it more reliable
5. classifiers can be used as feature extractors by cutting the network at earlier layers
   * the last pooling layer is most commonly used for feature extraction
   * best to use classifiers that have been trained on large datasets (ImageNet)
   * commonly used feature extractor: `Inception-v3` classifier
   * these features are called embedding
   * compare embedding to get the feature distance
6. Frechet Inception distance (FID)
   * FID calculates the difference between reals and fakes
   * FID uses the inception model and multivariate normal Frechet distance
   * real and fake embedding are two multivariate normal distributions
   * NO interpretable range for FID values
   * sample size needs to be large for FID to work well
   * FID is typically lower for larger sample sizes
7. Inception Score
   * entropy
   * KL divergence: conditional distribution (fidelity), marginal distribution (diversity)
   * try to capture fidelity and diversity
   * shortcoming: can be gamed too easily (generate one realistic image of each class), only looks at fake images (not reals), ImageNet doesn't teach a model all features
   * worse than FID
8. sampling and truncation
   * fakes are sampled using the training or prior distribution of z
   * truncate more for higher fidelity, lower diversity
   * human evaluation is still necessary for sampling
   * crowdsourced evaluation from Amazon Mechanical Turk
   * HYPE-time, HYPE-infinty
9. precision and recall
   * precision is to fidelity as to recall is to diversity
   * models tend to be better at recall
   * use truncation trick to improve precision
10. perceptual path length (PPL)
    * perceptual similarity, The Unreasonable Effectiveness of Deep Features as a Perceptual Metric, [arxiv](https://arxiv.org/abs/1801.03924)
11. reading material
    * a note on the inception score, [arxiv](https://arxiv.org/abs/1801.01973)
    * HYPE, A Benchmark for Human eYe Perceptual Evaluation of Generative Models, [arxiv](https://arxiv.org/abs/1904.01121)
    * Improved Precision and Recall Metric for Assessing Generative Models, [arxiv](https://arxiv.org/abs/1904.06991)
    * FID, Jean2018, [link](https://nealjean.com/ml/frechet-inception-distance/), [core.ac.uk](https://core.ac.uk/reader/82269844)
    * how to measure GAN performance, [medium.com](https://medium.com/@jonathan_hui/gan-how-to-measure-gan-performance-64b988c47732)
    * Large Scale GAN Training for High Fidelity Natural Image Synthesis, [arxiv](https://arxiv.org/abs/1809.11096)
    * are GANs created equal, a large-scale study, [arxiv](https://arxiv.org/abs/1711.10337)

## week6 GAN disadvantages and bias

1. GAN advantage: amazing empirical results, fast inference
2. GAN disadvantage
   * lack of intrinsic evaluation metrics
   * unstable training
   * no density estimation: necessary for finding anomalies
   * inverting is not straightforward: for image editing
3. alternatives to GAN
   * VAE: often lower fidelity results, density estimation, inversion, stable training
   * autoregressive models
   * flow models
   * hybrid models
4. machine bias
   * machine learning bias has a disproportionately negative effect on historically underserved populations
   * proprietary risk assessment software: difficult to validate, misses important considerations about people
   * COMPAS algorithm
5. fairness
   * fairness is difficult to define
   * no single definition of fairness
   * important to explore these before releasing a system into production
   * A Survey on Bias and Fairness in Machine Learning, [arxiv](https://arxiv.org/abs/1908.09635)
   * Does Object Recognition Work for Everyone, [arxiv](https://arxiv.org/abs/1906.02659)
   * What a machine learning tool that turns Obama white can (and can’t) tell us about AI bias, [theverge.com](https://www.theverge.com/21298762/face-depixelizer-ai-machine-learning-tool-pulse-stylegan-obama-bias)
   * bias can be introduced into a model at each step of the process: no variation in who or what is represented, bias in collection methods, diversity of the labellers, images can be biased to reflect "correctness" in the dominant culture
   * awareness and mitigation of bias is vital to responsible use of AI and state-of-the-art GANs
   * PULSE: Self-Supervised Photo Upsampling via Latent Space Exploration of Generative Models, [arxiv](https://arxiv.org/abs/2003.03808)
   * Mitigating Unwanted Biases with Adversarial Learning, [arxiv](https://arxiv.org/abs/1801.07593)
   * tutorial on fairness accountability transparency and ethics in computer vision at CVPR2020, [link](https://sites.google.com/view/fatecv-tutorial/home?authuser=0)
6. reading material
   * VAE, [VAE-note0](https://deepgenerativemodels.github.io/notes/vae/), [VAE-note1](http://www.cs.toronto.edu/~rgrosse/courses/csc421_2019/slides/lec17.pdf)
   * VAE-GAN, Autoencoding beyond pixels using a learned similarity metric, [arxiv](https://arxiv.org/abs/1512.09300)
   * hyperspherical Variational auto-encoders, [arxiv](https://arxiv.org/abs/1804.00891)
   * VQ-VAE2, Generating Diverse High-Fidelity Images with VQ-VAE-2, [arxiv](https://arxiv.org/abs/1906.00446)
   * autoregressive models, Conditional Image Generation with PixelCNN Decoders, [arxiv](https://arxiv.org/abs/1606.05328)
   * Glow: Better Reversible Generative Models, [openai](https://openai.com/blog/glow/)

## week7 StyleGAN and advancements

1. main improvements
   * stability: longer training and better images; WGAN, WGAN-GP, spectral normalization, average on the weights, progressive growing
   * capacity: larger models and higher resolution images; models, GPU, dataset
   * diversity: increasing variety in generated images; dataset
2. styleGAN goals
   * greater fidelity on high-resolution images
   * increased diversity of outputs
   * more control over image features
3. styleGAN
   * both W-loss and original loss works, just try it
   * style: any variation in the image, from larger, coarser styles to finer, more detailed styles
   * mapping network, styleGAN generator, adaptive instance normalization, progressive growing
4. Progressive Growing
   * Progressive Growing gradually doubles image resolution
   * helps with faster, more stable training for higher resolutions
5. noise mapping network
   * multilayer perceptron
   * map noise vector (z-space) to a less disentangled representation (w-space)
   * the intermediate noise vector is used as inputs to the generator
6. adaptive instance normalization (AdalN)
   * normalize convolution outputs using instance normalization
   * apply adaptive styles using the intermediate noise vector
   * AdalN transfes style information into the generated image from the intermediate noise vector
   * instance normalization is used to normalize individual examples before applying style statistics from the intermediate noise vector
7. style mixing and stochastic noise
   * style mixing increase diversity that the model sees during training
   * stochastic noise causes small vriations to output
   * coarse or fineness depends where in the network style or noise is added: earlier for coarser variation, later for finer variation
8. styleGAN2
   * demodulation, path length regularization, perceptual path length (PPL)
   * droplet artifects
9. reading material
   * The Unusual Effectiveness of Averaging in GAN Training, [arxiv](https://arxiv.org/abs/1806.04498)
   * FFHQ datasets
   * ProGAN, Progressive Growing of GANs for Improved Quality, Stability, and Variation, [arxiv](https://arxiv.org/abs/1710.10196)
   * styleGAN, A Style-Based Generator Architecture for Generative Adversarial Networks, [arxiv](https://arxiv.org/abs/1812.04948)
   * styleGAN2, Analyzing and Improving the Image Quality of StyleGAN, [arxiv](https://arxiv.org/abs/1912.04958)
   * CoGAN, Coupled Generative Adversarial Networks, [arxiv](https://arxiv.org/abs/1606.07536)
   * group normalization, [arxiv](https://arxiv.org/abs/1803.08494), [medium.com](https://medium.com/syncedreview/facebook-ai-proposes-group-normalization-alternative-to-batch-normalization-fb0699bffae7)
   * Pix2Pix
   * CycleGAN
   * GauGAN, Semantic Image Synthesis with Spatially-Adaptive Normalization, [arxiv](https://arxiv.org/abs/1903.07291)
   * BigGAN, Large Scale GAN Training for High Fidelity Natural Image Synthesis, [arxiv](https://arxiv.org/abs/1809.11096)
