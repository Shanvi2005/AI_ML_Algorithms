# -*- coding: utf-8 -*-
"""PrincipalComponentAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13k6FRcfles67K3ac02SQILjd97P6Zji_
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# %matplotlib inline

#Load dataset
from sklearn.datasets import load_breast_cancer

cancer_dataset=load_breast_cancer()

cancer_dataset.keys()

print(cancer_dataset.DESCR)

# the data key will have all the data
df=pd.DataFrame(cancer_dataset['data'],columns=cancer_dataset['feature_names'])
df.head()

#Standardisation -> in pca we first do feature scaling and we do standardisation before it
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

scaler.fit(df)

scaled_data=scaler.transform(df)

scaled_data

# we will extract only 2 feature from all the given

#Apply PCA Algorithm
from sklearn.decomposition import PCA

pca=PCA(n_components=2)

data_pca=pca.fit_transform(scaled_data)
data_pca

pca.explained_variance_

# pca=PCA() # if we remove n_components then it takes all features

# pca.fit_transform(scaled_data)

# pca.explained_variance_ # here if we add these values it can give a value near 100

plt.figure(figsize=(8,6))
plt.scatter(data_pca[:,0],data_pca[:,1],c=cancer_dataset['target'],cmap='plasma')
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")