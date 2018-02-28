# -*- coding: utf-8 -*-

from fastFM.datasets import make_user_item_regression
from sklearn.model_selection import train_test_split
import math
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import jcml.sys.myRedis as rd
from StringIO import StringIO
from fastFM import sgd
from sklearn.utils import shuffle

# This sets up a small test dataset.
# X, y, _ = make_user_item_regression(label_stdev=.4)
# X_train, X_test, y_train, y_test = train_test_split(X, y)

from fastFM import als
Rd = rd.myRedis()
test = Rd.get_csv_cache('test.csv')
train = Rd.get_csv_cache('train.csv')[0:400000]
train = shuffle(train)
print "data is loaded..."
v = DictVectorizer()
X_origin = train.loc[:,['iid','uid','time']].astype(np.string_).to_dict(orient='records')
X = v.fit_transform(X_origin)
y = np.array(train.loc[:,['score']]).flatten()
X_train, X_test, y_train, y_test = train_test_split(X, y)
print "start fit"
#fm = als.FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)
fm = sgd.FMRegression(n_iter=1000, init_stdev=0.1, l2_reg_w=0,
                          l2_reg_V=0, rank=2, step_size=0.1)
fm.fit(X_train, y_train)
print "start predict"
y_pred = fm.predict(X_test)
ground_truth = np.around(y_pred)

from sklearn.metrics import mean_squared_error

print 'mse:', mean_squared_error(np.array(y_test), y_pred)

R_real = math.sqrt(mean_squared_error(y_test,y_pred))

R_max  = math.sqrt(mean_squared_error(y_test,np.where(y_test>2.5,0,5)))

score  =((R_max-R_real)/R_max)*10

print score

#print "error sample/ all sample: " + str(float(np.sum(np.array(y_test)!=np.array(ground_truth)))/float(np.array(y_test).__len__()))

pass