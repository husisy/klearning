# deeplearning AI - Andrew Ng

## Week 1 Neural Networks and Deep Learning

1. hyperparameter tuning
2. regularization
3. momentum armrest prop
4. ad authorization
5. holdout cross-validation
6. end-to-end deep learning
7. recurrent neural networks (RNN) and LSTM
8. ReLU (rectified linear units)
9. supervised learning: house features, Ad. user info, Image recognition, Audio recognition, language translation, autonomous driver system
10. structured/unstructured data
    * structured: database of data (age, house size)
    * unstructured: audio, image, text
11. scale drives deep learning progress
12. Geoffrey Hinton (Langer Higgins), Don Norman, David Rumelhart, restricted Boltzman machine

## week 2

1. logistic regression, binary classification: X column为一个sample；W, b分开
2. squared loss function for logistic problem is not-convex
3. loss function / cost function
   * loss function: $L\left( \hat{y},y \right)$
   * cost function: $J\left( w,b \right)$
4. computation graph
5. SIMD (single instruction multiple data)
6. vectorization
7. broadcasting: `(2,) + (2,1) = (2,2); (2,) + (1,2) = (1,2)`
8. alway use 2-d array, rather then 1-d
9. learning rate, number of iterations, initialization methods, preprocessings
10. Pieter Abbeel interview, deep reinforcement learning

## week 3

1. activation function: sigmoid / tanh / ReLU / Leaky ReLU
2. initialize $W$ randomly with small value
3. Ian Goodfellow, GAN, adversarial examples, machine learning security

## week 4

1. deep neural network
2. hyperparameters: learning rate, number of iterations, number of hidden layer, number of hidden units, activation funtion, momentum, batch size, regulazation form/value, exponentially weighted beta, decay rate, batch normalization beta, batch normalization gamma

## week 5 Improving Deep Neural Networks

1. train set
2. hold-out cross validation / develop set, a small subset if large data set (10000 of 1000000)
3. test set
4. make sure develop set and test set come from same distribution
5. base (optimal) error
6. high bias: bigger network, train longer, neural network architecture search
7. high variance: more data, regularization, neural network architecture search
8. bias-variance tradeoff (not for deep learning)
9. $L_1$ regularization: $w$ will be sparse
10. $L_2$ regularization: Frobenius norm, weight decay
11. inverted dropout, no dropout in test, spread out weight
12. data augmentation
13. early stopping, orthogonalization
14. normalizing inputs
15. data vanishing and exploding gradient: weight randomly initializing, Xavier initialization, He initialization (for ReLU)
16. Yoshua, word embedding, unsupervised learning, RBM

## week 6

1. mini-batch: epoch, size of mini-batch ($2^n$, the way computer memory is layed out)
2. batch gradient descent: too long (when train sample size <2000)
3. mini-batch gradient descent:
4. stochastic gradient descent: lose vectorization
5. exponentially weighted averages: $v_i = \beta v_{i-1} + \left( 1-\beta \right) \theta_i$
6. bias correction
7. gradient with momentum
8. RMSprop: root mean square propagation, no need bias correction
9. Adam (Adaptive Momentum Estimation) optimization algorithm: learning rate, momentum beta (0.9), rmsprop beta (0.999), do need bias correction for both Vdw and Sdw
10. learning rate decay
11. local optima
12. saddle point
13. plateaus
14. 林元庆Li Yuanqing, China National's Lab, PaddlePaddle, phrase recognition, surveillance

## week 7

1. tunning order
   * learning rate
   * Adam beta (default is good)
   * mini-batch size (more efficiently)
   * hidden units
   * layers
   * learning rate decay
2. hyperparameter space chosen randomly at suitable scale
3. CV: convnet, ResNets
4. batch normalization
   * Sergey Loffe and Christian Szegedy
   * convariate shift
   * limits the amount which updating the parameters in the previous layers can affect the distribution of the value
   * slight regularization effect
   * estimate using exponentially weighted average (across mini-batch)
5. softmax regression
   * softmax function - hard max function
6. deep learning frameworks
   * Caffe/Caffe2
   * CNTK
   * DL4J
   * Keras
   * Lasagne
   * mxnet
   * PaddlePaddle
   * TensorFlow
   * Theano
   * Torch
   * ease of programming (development and deployment)
   * running speed
   * truly open (open source with good governance and remains open for a long time)
7. TensorFlow

## week 8

1. orthogonalization
2. fit training set well on cost function, no bad than human-level performance
3. trying early stopping first is not a good idea, since it affects the performance on training and dev set simualtaneously
4. single metric: precesion, recall, F1 score
5. satisficing and optimizing metrics, threshhold
6. train/dev/test data set should come from the same distribution
7. 1000000: train/dev/test = 990000/10000/10000
8. evaluation metrics, weight
   * define a metric to evaluate classifiers
   * tune weight to do well on this metric
9. human level performance
   * get labeled data from humans
   * gain insight from manual error analysis
   * better analysis of bias / variance
10. Bayes optimal error
11. avoidable bias
    * bigger model
    * train longer / better optimization algorithm
    * neural network architecture / hyperparameter search
12. variance
    * more data
    * regularization / dropout / data augmentation
    * neural network architecture / hyperparameter search
13. Andrej Karpathy, ImageNet, pretrained fine-tuning, transfer learning, openAI

## week 9

1. error analysis
2. mislabeled examples: deep learning are rebust to random error
   * apply same process to dev/test set to make sure they continue to come from the same distribution
   * consider examining examples your algorithm got right as well as ones it got wrong (not always done)
   * train and dev/test data set may now come from slightly different distribution
3. build your first system quickly, then iterate
4. data mismatch
   * train / train-dev / dev / test
   * error analysis
   * artificial data synthesis
5. transfer learning: pre-training, fine tuning
6. multi-task learning
   * training on a set of tasks that could benefit from having shared lower-level features
   * usually: amount of data you have for each task is quite similar
   * can train a big enough neural network to do well on all the tasks
7. end-to-end deep learning
   * pros: let the data speak, less hand-designing of components needed
   * cons: need large amount of data, exclude potentially useful hand-designed components
   * key: have sufficient data to learn a function of the complexity needed to may x to y?
8. substep of deep learning
   * estimating child's age from x-ray images: images->bones length->age
   * face recognition: detect face, person identification
9. Ruslan Salakhutdinov: restricted Boltzman Machines, Generative adversial network, variational auto-encoders

## week10, foundations of convolutional neural networks

1. task: image classification, object detection, style transfer
2. convolution
   * kernel / filter, channel / depth
   * Sobel filter: `[[1,2,1],[0,0,0],[-1,-2,-1]]`
   * scharr filter: `[[3,10,3],[0,0,0],[-3,-10,-3]]`
   * no padding: shrink output, throw a lot of information from the edge
   * image size `n`, kernel size `k`, stride `s`
   * valid padding: output size `(n-k)//s+1`
   * same padding: output size `(n-k+2p)//s+1`
   * kernel size are almost odd (not even): center of position, otherwise the padding will be "strange" (asymmetric padding)
   * cross correlation vs convolustion
   * `(H,W,C1)` + `(K,K,C1,C2)` -> `(h,w,C2)`
   * channels first, channels last
3. pooling
   * max pooling, average pooling (seldom, used in last few layers to collapse height and width dimension)
   * kernel size, stride
   * if feature detected in this region, then keep the high number
   * no parameter
   * padding seldom used in pooling
4. LeNet-5
5. advantage
   * parameter sharing
   * sparsity of connections
   * translation invariance

## week 11 case study

1. LeNet-5
   * average pooling
   * sigmoid / tanh
   * graph transformer network
2. AlexNet
   * ~60 million parameter
   * relu
   * two GPUs architecture
   * local response normalization
3. VGG
   * conv kernel=3x3 filter, stride=1, same padding
   * max pooling: kernel=2x2, stride=2
   * ~138 million parameter
4. ResNet
   * shortcut / skip connection
   * residual_v1: `a[l+2] = g(z[l+2]+a[l])`
   * motivation: in theory, deeper network should only help; however in reality, training error only get worse for a deeper network. (vanising and exploding gradients problem)
   * identity function is easy to learn for residual block to learn
5. network in network, `1x1` conv: change channel
6. inception network
   * input `(28,28,192)`, kernel1 `(1,1,192,64)`, kernel2 `(3,3,192,64)`, kernel3 `(5,5,192,32)`, max-pool (one by one conv later) `(28,28,32)`
   * to reduce 5x5 conv computation, use 1x1 first (bottleneck)
   * side branch
7. practice advice
   * pretrained weight (transfer learning)
   * data augmentation: mirroring, random cropping, rotation, shearing, color shifting (+RGB), PCA color augmentation (AlexNet)
   * loading data on the fly
   * data availbility (compared with problem complexity): object detection < image recognition < speech recognition
   * benchmark: ensembling, multi-crop at test time (10-crop)

## week 12 detection algorithms

1. task
   * object localization: one object
   * landmark (people pose estimation): output (x,y) coordinates of important points
   * object detection: multiple objects of different categories in the picture
2. output for classification with localization
   * probability: object of background; if background, then below (bbox and category) will not contribute to total loss
   * `(nx,ny,nh,nw)`: normalized (pixeled)
   * probability of categories
3. object detection
   * sliding windows detection: different size window
   * convolution implementation of sliding windows (OverFeat 2014): (weakness) the position of bbox is not going to be too accurate
4. You Only Look Once (YOLO)
   * assign the object to the grid cell containing the midpoint
   * output: `(grid,grid,C+5)
   * `(nx,ny,nh,nw)` are specified relative to grid cell, `(nx,ny)` in range `[0,1]`, `(nh,nw)` in range `[0,inf]`
   * problem: multiple object in single grid cell (using anchor to address)
   * real time object detection
5. intersection over union (IOU): correct if `IOU>0.5`
6. non-max suppression: `p_c * c_i`
   * independently carry out nms for each category
   * first discard all bbox with low probability (e.g. threshold 0.6)
7. anchor
   * predefined different size / ratio anchor
   * previously: each object in training image is assigned to grid cell that contains the object's midpoint
   * with anchor: each object in training image is assigned to grid cell that contains object's midpoint and anchor box for the grid cell with hightest IoU
   * problem: still cannot handle when objects in grid cell are more than the number of anchors (one anchor cannot assiciate with two objects)
   * using k-means to group together object shapes
8. region proposal
   * Region with CNN (RCNN)
   * segmentation algorithm (selective search)
   * Fast RCNN
   * Faster RCNN: use CNN to propose region

## week13 special applications face recognition and neural style transfer

1. task
   * face verification: `(image,name/ID) -> True/False`
   * face recognition: `(image, database) ->  one or None`
2. one shot learning
3. similarity function, threshold
4. Siamese network (DeepFace)
5. triplet loss (FaceNet)
   * anchor, positive, negative
   * margin
   * $L\left( A,P,N \right) =\max \left( \lVert f\left( A \right) -f\left( P \right) \rVert ^2-\lVert f\left( A \right) -f\left( N \right) \rVert ^2+\alpha ,0 \right) $
   * need multiple pictures of the same person
   * choose triplets that are hard to train on: increase the computational efficiency
6. face verification and binary classification
7. CNN visualization
   * pick a unit in layer 1, find nine image patches that maximize the unit's activation
   * recption region
8. neural style transfer: `(content,style) -> (generated image)`
   * initialize G randomly
   * use gradient descent to minimize `J(G)`
9. cost function
   * $J\left( G \right) =\alpha J_{content}\left( C,G \right) +\beta J_{style}\left( S,G \right) $
   * content cost function: $J_{content}\left( C,G \right) =\frac{1}{2}\lVert a^{\left[ l \right] \left( C \right)}-a^{\left[ l \right] \left( G \right)} \rVert ^2$
   * style cost function: define style as correlation between activations across channels; "high correlated" means whatever part of the image has this type of subtle vertical texture, that part of the image will probably have these orangish tint
   * Gram matrix: $G_{kk'}^{\left[ l \right] \left( S \right)}=\sum_{ij}{a_{ijk}^{\left[ l \right] \left( S \right)}a_{ijk'}^{\left[ l \right] \left( S \right)}}$; $G_{kk'}^{\left[ l \right] \left( G \right)}=\sum_{ij}{a_{ijk}^{\left[ l \right] \left( G \right)}a_{ijk'}^{\left[ l \right] \left( G \right)}}$
   * $J_{style}^{\left[ l \right]}\left( S,G \right) =\frac{1}{2}\lVert G^{\left[ l \right] \left( S \right)}-G^{\left[ l \right] \left( G \right)} \rVert ^2$
   * $J_{style}\left( S,G \right) =\sum_l{J_{style}^{\left[ l \right]}\left( S,G \right)}$
10. 1D / 2D / 3D convolution

## week 14 Recurrent Neural Networks

1. task
   * speech recognition: `(audio sequence) -> (token sequence)`
   * music generation: `(None) -> (audio sequence)`
   * sentiment classification: `(token sequence) -> (category)`
   * DNA sequence analysis: `(ATGC sequence) -> (protein sequence)`
   * machine translation: `(token sequence) -> (token sequence)`
   * video activity recognition: `(image sequence) -> (token sequence)`
   * named entity recognition: `(token sequence) -> (object sequence)`
2. notation: $x^{\left< t \right>}$
3. vocabulary: common size `30,000 ~ 100,000`
4. special token
   * `<UNKOWN>`
   * `<EOS>`: end of sentence, needed for language model
5. one-hot representantion
   * different length unless padding
   * doesn't share features learned across different positions of text
6. RNN
   * forward propogation: see `wiznote/NLP/RNN formula.md`
   * backpropagation through time
7. tanh more common than relu
8. architecture: many-to-many, many-to-one, one-to-many, one-to-one
9. languange model
   * sampling novel sequence
   * character-level language model
10. vanishing gradient problem
    * long-term dependency
11. Gated Recurrent Unit (GRU)
12. Long Short Term Memory (LSTM): update, forget, output, candidate
    * peephole LSTM
13. Bi-RNN
    * bad for speech recognition task
14. deep RNN

## week 15 word embeddings

1. featureized representation
2. word embedding
   * transfer learning
   * useful for analogy reasoning, NER, text summarization, co-reference resolution, parsing (Dependency parsing, contituent parsing)
   * less useful for language modeling, machine learning
   * relation to face encoding
3. t-SNE
4. analogy reasoning
   * similarity: cosine, Euclidian distance
5. learning word embedding
   * neural language model: predict next word
   * word2vec: skip-grams / CBOW
6. problem with softmax classification
   * hierarchical softmax: common words on top
   * remove stop words from train-set
   * negative sampling: `k=5~20`, sampling according to weight $f_{word}^{\text{3/}4}$, here $f$ is frequency
7. global vectors for word representation (GloVe)
   * $\text{minimize}\sum_{ij}{f\left( X_{ij} \right) \left( \theta _{i}^{T}e_j+b_i+b_j-\log X_{ij} \right) ^2}$
   * $e_{w}^{( final )} = (\theta_w+e_w) /2$
8. sentiment classification
9. dibiasing word embeddings
   * gender, ethnicity, sexual orientation bias: `(man, woman), (programmer, homemaker)`, `(father, mother), (doctor, nurse)`
   * identify bias direction: `e_he - e_she`
   * neutralize: for every word that is not definitional, project to get rid of bias
   * equalize pairs

## week 16 various sequence to sequence architectures

1. sequence to sequence
   * machine translation, image captioning
   * encoder, decoder
   * different from language model: conditional language model; pick the most likely sentence
   * greedy search, beam search
2. beam search
   * $\text{argmax} \frac{1}{T_{y}^{\alpha}}\sum_{t=1}^{T_y}{\log P\left( y^{\left< t \right>}|x,y^{\left< 1 \right>},...,y^{\left< t-1 \right>} \right)}$
   * length normalization
   * beam width
   * **error analysis**
3. BLEU score (bilingual evaluation understudy)
   * $P_n=\frac{\sum_{ngram\in \hat{y}}{count_{clip}\left( ngram \right)}}{\sum_{ngram\in \hat{y}}{count\left( ngram \right)}}$
   * brevity penalty (BP): BP = 1 if $L_{MT}>L_{reference}$ otherwise $\exp \left( 1-\frac{L_{MT}}{L_{reference}} \right)$
   * $BLEU = BP\exp \left( \frac{P_1+P_2+P_3+P_4}{4} \right)$
4. attention model *TBA*
5. speech recognition *TBA*
6. trigger word detection *TBA*
