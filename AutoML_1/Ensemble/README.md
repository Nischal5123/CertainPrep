# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                                 |   Weight |
|:--------------------------------------|---------:|
| 1_Linear_KMeansFeatures_BoostOnErrors |        1 |

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.666153  |  nan        |
| auc       | 0.541228  |  nan        |
| f1        | 0.561265  |    0.227053 |
| accuracy  | 0.619353  |    0.508827 |
| precision | 0.616822  |    0.5287   |
| recall    | 1         |    0.227053 |
| mcc       | 0.0964794 |    0.508827 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.666153  |  nan        |
| auc       | 0.541228  |  nan        |
| f1        | 0.139406  |    0.508827 |
| accuracy  | 0.619353  |    0.508827 |
| precision | 0.590643  |    0.508827 |
| recall    | 0.0790297 |    0.508827 |
| mcc       | 0.0964794 |    0.508827 |


## Confusion matrix (at threshold=0.508827)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1928 |               70 |
| Labeled as 1 |             1177 |              101 |

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
