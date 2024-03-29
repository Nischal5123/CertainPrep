# CertainPrep: Showcasing Minimal Imputations in ML Data Preparation

[CertainPrep.pdf](media%2FCertainPrep.pdf)

## Description
Real-world data often contains missing values, outliers, and inconsistency. To train accurate models over real-world datasets, users
need to spend a substantial amount of time and resources imputing
and finding proper values for cleaning data items. In this paper,
we demonstrate that it is possible to learn accurate models without data imputations for certain training data and target models.
We propose a unified approach for checking the necessity of data
imputation to learn accurate models across various widely used machine learning paradigms. Our CertainPrep system, built upon this
approach, checks this necessity efficiently with theoretical guarantees and returns accurate models in cases where imputation is
unnecessary. When imputation is required, the system recommends
minimal imputations. Our demonstration emphasizes interactivity
and performance characterization to showcase the time and effort
savings from data imputation while delivering accurate ML models.

# Run Configuration
- mercury add {path to notebook} eg: `mercury add certain-prep-training-view.ipynb`
- mercury run
- Web app opens in http://127.0.0.1:8000
