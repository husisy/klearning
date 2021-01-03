# Machine Learning - Andrew Ng

## week 1

ops

## week 2

Environment Setup Instructions

Multivariate Linear Regression

Computing Parameters Analytically

1. normal equation
   * design matrix: $X$
   * $\theta=\left( X^TX \right)^{-1}X^Ty$
   * no need to do feature scaling
2. normal matrix is not-invertible
   * redundant features (linearly-dependent)
   * too many features: delete some features or use regularization

| Aspect | Gradient Descent | Normal Equation |
| :--: | :--: | :--: |
| choose $\alpha$ | yes | no |
| iterate | yes | no |
| time complexity | $o\left( kn^2 \right)$ | $o\left( n^3 \right)$ |
| when $n$ is large| well | slow |

## week 3: classification and representation

1. linear regression do not work for classification: sensitive to data, output not in the range[0,1]
2. Decision boundary
3. cost function $C\left( h_\theta \left( x \right) ,y \right) = -y \log\left( h_\theta \left( x \right) \right) - \left( 1-y \right) \log \left( 1-h_\theta \left( x \right) \right)$
4. gradient descent: $\theta_j = \theta_j - \frac{\alpha}{m} \sum\limits_{i=1}^m {\left( h_\theta \left( x^{\left( i \right)} \right) - y^{\left( i \right)} \right){x^{\left( i \right)}}}$
5. conjugate gradient
6. BFGS
7. L-BFGS
8. overfitting
   * reduce feature: manually select features; model selection
   * regularization: reduce the maglitude of $\theta_j$
9. regularization parameter: $\min_\theta{\frac{1}{2m}\sum\limits_{i=1}^m {\left( h_\theta \left( x^{\left( i \right)} \right) - y^{\left( i \right)} \right)^2} + \lambda \sum\limits_{j=1}^n \theta_j^2 }$
10. gradient descent: $\theta_j = \left( 1-\alpha \frac{\lambda}{m} \right) \theta_j - \frac{\alpha}{m} \sum\limits_{i=1}^m {\left( h_\theta \left( x^{\left( i \right)} \right) - y^{\left( i \right)} \right){x^{\left( i \right)}}}$

## week 4 neural networks

1. dendrites, axons, sigmoid (logistic) activation function, weights/parameters, hidden layer
2. 已自己推导的公式
   * $J\left( \Theta \right) = \frac{1}{m} \sum\limits_{i=1}^m {\sum\limits_{k = 1}^K {\left[ -y_k^{\left( i \right)} \log \left( {h_\theta {\left( x^{\left( i \right)} \right)}_k} \right) - \left( 1-y_k^{\left( i \right)} \right)\log \left( 1-h_\theta{\left( x^{\left( i \right)} \right)}_k \right) \right] }} + \frac{\lambda}{2m} \sum\limits_{l=1}^{L-1} {\sum\limits_{i=1}^{s_l} {\sum\limits_{j=1}^{s_l+1} {{\Theta_{i,j}^{\left( l \right)}}^2}}}$
   * $\delta^{\left( l \right)}:= \frac{\partial J\left( \Theta \right)}{\partial z^{\left( l \right)}}$
   * $\delta^L = \frac{1}{m} \sum\limits_{i=1}^m {a^{\left( l \right)} - y^{\left( i \right)}}$
   * $\delta^l = \left( {\left( \Theta^{\left( l \right)} \right)}^T\delta^{l+1} \right).*a^{\left( l \right)}\left( 1-a^{\left( l \right)} \right)$
   * $D_{ij}^{\left( l \right)}:=\frac{\partial J\left( \Theta  \right)}{\partial \Theta_{ij}^{\left( l \right)}}=\delta^{\left( l+1 \right)}\left( a^{\left( l \right)} \right)^T+\left[ \frac{\lambda}{m} \Theta_{ij}^{\left( l \right)} \right]_{j \ne 0}$

## week 6

1. debugging a neural network
   * more training examples: high variance
   * smaller sets of features: high variance
   * additional features: high bias
   * polynomial features: high bias
   * increasing or decreasing $\lambda$
2. training set, cross validation set, test set
3. test set error: (different from cost function for classification)
4. learning curves
5. precision, recall, F1 score
