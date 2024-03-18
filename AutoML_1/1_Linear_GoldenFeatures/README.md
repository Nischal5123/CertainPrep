# Summary of 1_Linear_GoldenFeatures

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True
 - **random_seed**: 123

## Optimized metric
accuracy

## Training time

3.8 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.670211  |  nan        |
| auc       | 0.528581  |  nan        |
| f1        | 0.561265  |    0.214062 |
| accuracy  | 0.609585  |    0.490995 |
| precision | 0.496403  |    0.490995 |
| recall    | 1         |    0.214062 |
| mcc       | 0.0788538 |    0.438414 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.670211  |  nan        |
| auc       | 0.528581  |  nan        |
| f1        | 0.0973888 |    0.490995 |
| accuracy  | 0.609585  |    0.490995 |
| precision | 0.496403  |    0.490995 |
| recall    | 0.0539906 |    0.490995 |
| mcc       | 0.0458707 |    0.490995 |


## Confusion matrix (at threshold=0.490995)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1928 |               70 |
| Labeled as 1 |             1209 |               69 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
