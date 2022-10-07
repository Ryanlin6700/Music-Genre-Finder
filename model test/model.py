# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:10:01 2022

@author: User
"""
import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier, XGBRFClassifier
from xgboost import plot_tree, plot_importance

from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE

from sklearn.model_selection import cross_val_score

# 讀取完整csv檔
df_3s = pd.read_csv('allmusic3s.csv', index_col=0)
df_3s = df_3s.dropna()
#df_3s.isnull().sum().sort_values(ascending = False)
#df_3s

# label 重新編碼
df_3s['label']=df_3s['label'].replace(['blues','classical','country','disco','hiphop','jazz','metal','pop'
,'reggae','rock'],[0,1,2,3,4,5,6,7,8,9])
df_3s = df_3s.drop(['song_name'], axis=1)

# 分成特徵欄位及預測目標欄位
y = df_3s['label']
X = df_3s.loc[:, df_3s.columns != 'label'] # label以外的欄位
#### NORMALIZE X ####

# 對特徵值做標準化
cols = X.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X)

# 新dataframe用標準化過的特徵值
X = pd.DataFrame(np_scaled, columns = cols)

# 切成訓練集合測試集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)



# 模型
import time
def model_assess(model, title = "Default"):
    start = time.perf_counter()
    
    # train_test_split的切法
    #==============================
    # model.fit(X_train, y_train)   # 訓練模型
    # preds = model.predict(X_test)  # 測試模型
    # end = time.perf_counter()
    # print('Accuracy', title, ':', round(accuracy_score(y_test, preds), 5), '\n')  # print出模型準確率
    #==============================
    
    # k-fold的切法
    #==============================
    scores = cross_val_score(model, X, y, cv=3, scoring='accuracy')
    end = time.perf_counter()
    print("model(",title,")","\n"," >>> Accuracy: {} (mean) (+/- {} std)".format(round(scores.mean(),3), round(scores.std(),4) * 2))
    #==============================
    
    print("time:",round((end - start),2),"s") # 計算時長
    print("\n")
    
    # print(confusion_matrix(y_test, preds))
 

# =============================================================================
# # Naive Bayes
# nb = GaussianNB()
# model_assess(nb, "Naive Bayes")
# 
# # Stochastic Gradient Descent
# sgd = SGDClassifier(max_iter=5000, random_state=0)
# start = time.perf_counter()
# model_assess(sgd, "Stochastic Gradient Descent")
# 
# # KNN
# start = time.perf_counter()
# knn = KNeighborsClassifier(n_neighbors=19)
# model_assess(knn, "KNN")
# 
# # Decission trees
# start = time.perf_counter()
# tree = DecisionTreeClassifier()
# model_assess(tree, "Decission trees")
# 
# # Random Forest
# rforest = RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0)
# model_assess(rforest, "Random Forest")
# 
# # Support Vector Machine
# svm = SVC(decision_function_shape="ovo")
# model_assess(svm, "Support Vector Machine")
# =============================================================================

# Logistic Regression
# lg = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
# model_assess(lg, "Logistic Regression")
# ************************************************************* 錯誤碼
# * ConvergenceWarning: lbfgs failed to converge (status=1):  *
# * STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.              *   
# *************************************************************

# =============================================================================修正了
# lg = LogisticRegression(solver='lbfgs', multi_class='multinomial',max_iter=10000)  # max_iter=10000 解決錯誤待研究問題
# model_assess(lg, "Logistic Regression")
# =============================================================================


# Neural Nets
# nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5000, 10), random_state=1)
# model_assess(nn, "Neural Nets")
# ************************************************************* 錯誤碼
# * ConvergenceWarning: lbfgs failed to converge (status=1):  *
# * STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.              *   
# *************************************************************

nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5000, 10), max_iter=1000)
model_assess(nn, "Neural Nets")

# =============================================================================
# # Cross Gradient Booster
# xgb = XGBClassifier(n_estimators=1000, learning_rate=0.05)
# model_assess(xgb, "Cross Gradient Booster")
# 
# # Cross Gradient Booster (Random Forest)
# xgbrf = XGBRFClassifier(objective= 'multi:softmax')
# model_assess(xgbrf, "Cross Gradient Booster (Random Forest)")
# =============================================================================
