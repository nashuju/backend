# -*- coding: utf-8 -*-

from fastFM.datasets import make_user_item_regression
from sklearn.model_selection import train_test_split
import math
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import jcml.sys.myRedis as rd
from StringIO import StringIO
from sklearn.externals import joblib

# This sets up a small test dataset.
# X, y, _ = make_user_item_regression(label_stdev=.4)
# X_train, X_test, y_train, y_test = train_test_split(X, y)

from fastFM import als
Rd = rd.myRedis()
test = Rd.get_csv_cache('test.csv')
train = Rd.get_csv_cache('train.csv')[0:100000]
print "data is loaded..."
v = DictVectorizer()
#X_origin = train[0:1000].loc[:,['uid','iid']].astype(np.string_).to_dict(orient='records')
X_merge=pd.concat([train.loc[:,['uid','iid']],test])
X_merge_hot=v.fit_transform(X_merge.astype(np.string_).to_dict(orient='records'))
train_hot = X_merge_hot[0:train.shape[0]]
test_hot = X_merge_hot[train.shape[0]:X_merge_hot.shape[0]]

#X = v.fit_transform(X_origin)
y = np.array(train.loc[:,['score']]).flatten()
#X_train, X_test, y_train, y_test = train_test_split(X, y)
print "start fit"
fm = als.FMRegression(n_iter=100, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)
fm.fit(train_hot, y)
joblib.dump(fm,"fast_fm_module_12_16.m")
print "start predict"
y_pred = fm.predict(test_hot)

df_fm = pd.DataFrame(y_pred,columns=['score'])
df_fm.to_csv("fast_fm_10_0000_12_16.csv",index=False)
print y_pred.shape

from sklearn.metrics import mean_squared_error
print 'mse:', mean_squared_error(test, y_pred)

R_real = math.sqrt(mean_squared_error(test,y_pred))

R_max  = math.sqrt(mean_squared_error(test,test))

score  =((R_max-R_real)/R_max)*10

print score

pass