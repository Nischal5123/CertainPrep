# MinPrep: Showcasing Minimal Imputations in ML Data Preparation
## Description
Real-world data often contains dirty data such as missing values,
outliers, and inconsistencies. To train accurate models over real-world datasets, users need to spend a substantial amount of time
and resources imputing and finding proper values for cleaning training examples. This paper demonstrates the approach to learning
accurate models without data imputations for certain training data
and machine learning models. We propose a unified approach for
checking the necessity of data imputation to learn accurate models
across various widely used machine learning paradigms, allowing
users to define their requirements for a model’s accuracy. Built upon
this approach, our MinPrep system checks this necessity efficiently
with theoretical guarantees and returns accurate models in cases
where imputation is unnecessary. When imputation is required, the
system recommends minimal training examples to impute and involves users in trying different imputation methods and comparing
them. Our demonstration emphasizes the time and manual effort
savings from avoiding data imputation while delivering accurate
machine learning models.

![MinPrep.png](media%2FMinPrep.png)
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


## Citation
```
@article{10.1145/3654929,
author = {Zhen, Cheng and Aryal, Nischal and Termehchy, Arash and Chabada, Amandeep Singh},
title = {Certain and Approximately Certain Models for Statistical Learning},
year = {2024},
issue_date = {June 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {2},
number = {3},
url = {https://doi.org/10.1145/3654929},
doi = {10.1145/3654929},
journal = {Proc. ACM Manag. Data},
month = {may},
articleno = {126},
numpages = {25},
keywords = {data preparation, data quality, uncertainty quantification}
}
```
