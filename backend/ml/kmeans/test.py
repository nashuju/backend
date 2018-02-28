# -*- coding: utf-8 -*-

from pyfm import pylibfm
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import math
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')
v = DictVectorizer()
X_origin = train[0:10000].loc[:,['iid','uid','time']].astype(np.string_).to_dict(orient='records')
X = v.fit_transform(X_origin)
y = np.array(train[0:10000].loc[:,['score']]).flatten()
X_train, X_test, y_train, y_test = train_test_split(X, y)
print "data is ready"
fm = pylibfm.FM(num_factors=100, num_iter=10, verbose=True, task="regression", initial_learning_rate=0.01, learning_rate_schedule="optimal")
y_train = y_train.astype(np.float64)
fm.fit(X_train,y_train)
print 'fit well'
preds = fm.predict(X_test)
ground_truth = np.around(preds)
print "mean_squared_error:"
R_real = math.sqrt(mean_squared_error(y_test,preds))


R_max  = math.sqrt(mean_squared_error(y_test,np.where(y_test>2.5,0,5)))

score  =((R_max-R_real)/R_max)*10

print score

print y_test
print "error sample/ all sample: " + str(float(np.sum(np.array(y_test)!=np.array(ground_truth)))/float(np.array(y_test).__len__()))


pass