import pandas as pd 
import numpy as np 
import random
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt 
from sklearn.metrics import precision_recall_curve
from sklearn.metrics.pairwise import cosine_similarity as sm 
from sklearn.metrics import roc_auc_score, roc_curve, auc
from sklearn.metrics import classification_report as clfr
from sklearn.metrics import confusion_matrix as cm

print("Test for Databricks implementation of Github repo!")

data = pd.read_csv("output.txt", header=None)
Value = roc_auc_score(df[2], df[3])
print("auc: " + str(Value))

fpr, tpr, thresholds = roc_curve(df[2], df[3], pos_label=1)
plt.plot([0, 1], [0, 1], linestyle='--')
plt.plot(fpr,tpr,label="auc:" + str(Value))
plt.title("auc-roc curve")
plt.grid()
plt.show() 

tpr = pd.DataFrame(tpr)
fpr = pd.DataFrame(fpr)
thres = pd.DataFrame(thresholds)
frames = [tpr, fpr, thres]
data = pd.concat(frames, axis=1, ignore_index=True)
data.columns = ['tpr', 'fpr', 'thres']
data.head()

data[['tpr','fpr','thres']].plot(grid=1, ylim=(0,1), figsize=(10,5))