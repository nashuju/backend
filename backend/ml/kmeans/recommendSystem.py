# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import jcml.sys.myRedis as rd
from StringIO import StringIO
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from numpy import linalg as la
from math import sqrt
A=np.mat([[1,2,3],[4,5,6]])
U,sigma,VT=la.svd(A)
Rd = rd.myRedis()
test = Rd.get_csv_cache('test.csv')
train = Rd.get_csv_cache('train.csv')
# train = shuffle(train)
# train = train[0:100000]
# trainArray = np.array(train)
# length = trainArray.__len__()
# X_train = train.head((int)(-length*0.7))
# y_train = train['score'].head((int)(-length*0.7))
#
# X_test = (train.loc[:,['uid','iid']]).tail((int)(-length*0.3))
# y_test = (train['score']).tail((int)(-length*0.3))

#按照uid进行分组取,并score值取平均
rate_rank = train.groupby('uid').mean().loc[:,['score']].iloc[:,-1]

rate_rank=pd.DataFrame(np.int32((rate_rank*2).values),index=rate_rank.index,columns=['group'])

rate_rank_des = rate_rank.reset_index()

train_plus =pd.merge(train,rate_rank_des,how='left',on='uid')

test_plus =pd.merge(test,rate_rank_des,how='left',on='uid')

res =train_plus.groupby(['iid','group']).mean().reset_index().loc[:,['iid','group','score']]

result6 =pd.merge(test_plus,res,how='left',on=['iid','group']).fillna(3.0)


# rate_rank = X_train.groupby('uid').mean().loc[:,['score']].iloc[:,-1]
#
# rate_rank=pd.DataFrame(np.int32((rate_rank*2).values),index=rate_rank.index,columns=['group'])
#
# rate_rank_des = rate_rank.reset_index()
#
# train_plus =pd.merge(X_train,rate_rank_des,how='left',on='uid')
#
# test_plus =pd.merge(X_test,rate_rank_des,how='left',on='uid')
#
# res =train_plus.groupby(['iid','group']).mean().reset_index().loc[:,['iid','group','score']]
#
# result6 =pd.merge(test_plus,res,how='left',on=['iid','group']).fillna(3.0)
#
# print mean_squared_error(y_test,result6['score'])
#
# def rmse(prediction, ground_truth):
#     ground_truth = np.around(ground_truth)
#     print float(np.sum(np.array(prediction)!=np.array(ground_truth)))/float(np.array(prediction).__len__())
#     return sqrt(mean_squared_error(prediction, ground_truth))
#
# rmse(y_test,result6['score'])
#
# preds = result6['score']
#
# R_real = sqrt(mean_squared_error(y_test,preds))
#
# R_max  = sqrt(mean_squared_error(y_test,np.where(y_test>2.5,0,5)))
#
# score  =((R_max-R_real)/R_max)*10
#
# print score

pass