# Simple Image classification using SVM with feature extraction and selection.

## Papers:
[SVM - Vapnik et al.,](https://link.springer.com/article/10.1007/BF00994018)

## Dataset:
    - [MNIST fashion](https://www.kaggle.com/datasets/zalando-research/fashionmnist)
    - [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html)

## Baseline: 
    CNN are state of the art

## What we will do:
    - Simple SVM.
    - With feature extraction or selection - Recursive feature elimination, something else???
        - SVM with autoencoder
        - SVM + RFE
        - SVM + [Relief](https://medium.com/@yashdagli98/feature-selection-using-relief-algorithms-with-python-example-3c2006e18f83)

    - Compare performance & training time of SVM models with CNN 

---
### Different types of Regression
- Quantile Regression
- Ridge
- Lasso
- Elastic Net
- Principle Components Regression
- Partial Least
- Support Vector Regression
- Negative Binomial
- Quasi Poisson
- Cox Regre
- Tobit Regr

### Different Loss funcs
Regression loss -->
- MSE
- MAE
- Huber loss
- Log Cosh loss
- Quantile loss

Classification loss -->
- Hinge/ Multiclass SVM loss
- Cross entropy / Negative log likelihood
- KL Divergence