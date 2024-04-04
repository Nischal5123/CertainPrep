# CertainPrep: Showcasing Minimal Imputations in ML Data Preparation
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

![CertainPrep.png](media%2FCertainPrep.png)
The data-view (A)
provides data import and automatically populates possible features
and targets. Users can also manually modify input features and
the target label. The data-exploration view (B) presents a sample
of the dataset and summary visualizations. After performing an
exploratory analysis of the data, the user may define the ML model
training configuration. Model-configuration panel (C) allows users
to select the ML model to train, specify if they also want to evaluate
ACM, provide ACM threshold, and set a verbose output returning a dirty sample that needs attention. Additionally, the analyst
can provide a custom cleaning function (D) that CertainPrep can
incorporate into the data preparation pipeline when CMs do not
exist. After the analyst initiates training, the result view (E) 



# Run Configuration
- make sure required packages are installed in requirement.txt. Specially: pip install notebook , pip install mercury
- mercury add {path to notebook} eg: `mercury add certain-prep-training-view.ipynb`
- mercury run
- Web app opens in http://127.0.0.1:8000
