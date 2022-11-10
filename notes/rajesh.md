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
- (Quantile Regression)[https://towardsdatascience.com/quantile-regression-ff2343c4a03]
- Ridge
- Lasso
- (Elastic Net)[https://machinelearningmastery.com/elastic-net-regression-in-python/]
    - https://python.plainenglish.io/ridge-lasso-elasticnet-regressions-from-scratch-32bf9f1a03be
- Principle Components Regression
- (Partial Least Square)[https://www.xlstat.com/en/solutions/features/partial-least-squares-regression#:~:text=The%20Partial%20Least%20Squares%20regression,used%20to%20perfom%20a%20regression.&text=Some%20programs%20differentiate%20PLS%201,is%20only%20one%20dependent%20variable.]
- Support Vector Regression
- [Negative Binomial](https://data.library.virginia.edu/getting-started-with-negative-binomial-regression-modeling/)
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

----

## Proposal: Analysing different regression models using different loss functions & regularizers
Models = Elastic Net Regr, Quasi Poisson Regr