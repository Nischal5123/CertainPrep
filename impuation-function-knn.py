from sklearn.impute import KNNImputer
import time
import numpy as np
import pandas as pd

def get_knn_imputer_model_classification(training_data):
    X_train=training_data
    start_time_s = time.time()

    # Simple imputation using mean strategy for each column
    imputer = KNNImputer(missing_values=np.nan)
    imputed_X=imputer.fit_transform(X_train)

    # Assert that there are no more null values in X_train
    assert not pd.DataFrame(imputed_X).isnull().any().any()
    return imputed_X

