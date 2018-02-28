# -*- coding: utf-8 -*-

from pyfm import pylibfm
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.externals import joblib

import math
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')[0:100000]
v = DictVectorizer()
# X_origin = train.loc[:,['iid','uid']].astype(np.string_).to_dict(orient='records')
# X = v.fit_transform(X_origin)
y = np.array(train.loc[:,['score']]).flatten().astype(np.float64)
#X_train, X_test, y_train, y_test = train_test_split(X, y)

X_merge=pd.concat([train.loc[:,['uid','iid']],test])
X_merge_hot=v.fit_transform(X_merge.astype(np.string_).to_dict(orient='records'))
train_hot = X_merge_hot[0:train.shape[0]]
test_hot = X_merge_hot[train.shape[0]:X_merge_hot.shape[0]]

print "data is ready"
fm = pylibfm.FM(num_factors=100, num_iter=30, verbose=True, task="regression", initial_learning_rate=0.01, learning_rate_schedule="optimal")
#y_train = y_train.astype(np.float64)
fm.fit(train_hot,y)
print 'fit well'
joblib.dump(fm,"fm_model10,0000_iter_30.m")

print "start predict"
y_pred = fm.predict(test_hot)

df_fm = pd.DataFrame(y_pred,columns=['score'])
df_fm.to_csv("fm_result100_0000_iter_30.csv",index=False)

#
# ground_truth = np.around(preds)
#
# def rmse(prediction, ground_truth):
#     ground_truth = np.around(ground_truth)
#     print float(np.sum(np.array(prediction)!=np.array(ground_truth)))/float(np.array(prediction).__len__())
#     return math.sqrt(mean_squared_error(prediction, ground_truth))
#
# print rmse(y_test,preds)
#
#
# print y_test
# print "mean_squared_error:"
# print mean_squared_error(y_test,preds)
# print "error sample/ all sample: " + str(float(np.sum(np.array(y_test)!=np.array(ground_truth)))/float(np.array(y_test).__len__()))
#
R_real = math.sqrt(mean_squared_error(y_test,preds))

R_max  = math.sqrt(mean_squared_error(y_test,np.where(y_test>2.5,0,5)))

score  =((R_max-R_real)/R_max)*10

print score

