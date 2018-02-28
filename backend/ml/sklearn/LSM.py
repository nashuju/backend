# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
reg = linear_model.LinearRegression()
#reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
#线性拟合

train = pd.read_csv('HTRU_2.csv',names=['A','B','C','D','E','F','G','H',"result"])
train = shuffle(train)
trainArray = np.array(train)
length = trainArray.__len__()
X_train_array = np.array(train.loc[:,['A','B','C','D','E','F','G','H']])[:(int)(-length*0.7)]
y_train_array = np.array(train['result'])[:(int)(-length*0.7)]

X_test_array = np.array(train.loc[:,['A','B','C','D','E','F','G','H']])[(int)(-length*0.7):]
y_test_array = np.array(train['result'])[(int)(-length*0.7):]

# trainSet = trainArray[:-length*0.7]
# testSet  = trainArray[-length*0.7:]

reg.fit (X_train_array,y_train_array)

y_pred = reg.predict(X_test_array)

#print reg.coef_
threashold = 0.46

print "最小二乘法"
result_pred = np.where(y_pred>threashold,1,0)
Total_P = np.sum(result_pred==1)
TP = np.sum(result_pred[result_pred==y_test_array]==1)
FN = np.sum(result_pred[y_pred!=y_test_array]==0)
precision = float(TP)/float(Total_P)
recall = float(TP)/float(TP+FN)
print "TP: "+ str(TP)
print "Total_P: " + str(Total_P)
print "FN: "+ str(FN)
print ("precision:%.2f " % precision)
print ("recall:%.2f " % recall)
print ("f1:%.2f \n" % f1_score(y_test_array, np.where(y_pred>threashold,1,0)))


print "岭回归"
reg_ridge = linear_model.Ridge (alpha = .5)
reg_ridge.fit(X_train_array,y_train_array)
y_ridge_pred = reg_ridge.predict(X_test_array)

#print('Variance score: %.2f' % r2_score(y_test_array, y_ridge_pred))

result_pred = np.where(y_ridge_pred>threashold,1,0)
Total_P = np.sum(result_pred==1)
TP = np.sum(result_pred[result_pred==y_test_array]==1)
FN = np.sum(result_pred[y_ridge_pred!=y_test_array]==0)
precision = float(TP)/float(Total_P)
recall = float(TP)/float(TP+FN)
print "TP: "+ str(TP)
print "Total_P: " + str(Total_P)
print "FN: "+ str(FN)
print ("precision:%.2f " % precision)
print ("recall:%.2f " % recall)
print ("f1:%.2f \n" % f1_score(y_test_array, np.where(y_ridge_pred>threashold,1,0)))



for i in range(1,10,1):
      zero_df = train[train['result']==0];zero_array=np.array(zero_df);zero_len = zero_array.__len__()
      one_df  = train[train['result']==1];one_array=np.array(one_df);one_len=one_array.__len__()
      new_train = shuffle(pd.concat([one_df,zero_df[:one_len*i]]));length = new_train.__len__()
      X_train_array = np.array(new_train.loc[:,['A','B','C','D','E','F','G','H']])[:(int)(-length*0.7)]
      y_train_array = np.array(new_train['result'])[:(int)(-length*0.7)]

      X_test_array = np.array(new_train.loc[:,['A','B','C','D','E','F','G','H']])[(int)(-length*0.7):]
      y_test_array = np.array(new_train['result'])[(int)(-length*0.7):]


      print "N = %d 时:" % i
      reg_ridge = linear_model.Ridge (alpha = .5)
      reg_ridge.fit(X_train_array,y_train_array)
      y_ridge_pred = reg_ridge.predict(X_test_array)
      result_pred = np.where(y_ridge_pred>threashold,1,0)

      Total_P = np.sum(result_pred==1)
      TP = np.sum(result_pred[result_pred==y_test_array]==1)
      FN = np.sum(result_pred[result_pred!=y_test_array]==0)
      print "TP: "+ str(TP)
      print "Total_P: " + str(Total_P)
      print "FN: "+ str(FN)

      precision = float(TP)/float(Total_P)
      recall = float(TP)/float(TP+FN)
      print ("precision:%.2f " % precision)
      print ("recall:%.2f " % recall)
      print ("f1:%.2f \n" % f1_score(y_test_array, np.where(y_ridge_pred>threashold,1,0)))
