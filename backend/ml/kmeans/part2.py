# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

str = raw_input('max col number and row number:')
while str != '0 0':
    n = int(str[0]) #行数
    a = []
    for i in range(n):
        a.append(list(map(int, raw_input("input row %d:"%(i)).split())))
    a = np.array(a)
    df = pd.DataFrame(a,columns=[i for i in range(a.shape[1])])
    baseM =np.where(df==0,0,1)
    baseMDF = pd.DataFrame(baseM,columns=[i for i in range(a.shape[1])],copy=True)
    colMaxDF = pd.DataFrame(df.max())
    rowMaxDF = pd.DataFrame(df.T.max())
    colMax = df.max()
    rowMax = df.T.max()
    rowMaxlist = list(set(df.T.max()))
    row_value  = [v for k,v in rowMax.to_dict().items()]
    to_add = 0
    for k,v in colMax.to_dict().items():
        row = rowMaxDF[rowMaxDF[0]==v].index.tolist()
        col = k*np.ones((rowMaxDF[rowMaxDF[0]==v].index.tolist().__len__()))
        if v in rowMaxlist:
            baseMDF.loc[row,col] = v
        else:
            to_add += v-1
    for v in list(set(colMax)):
        if v in rowMaxlist:
            rowMaxlist.remove(v)
    to_add += np.sum(rowMaxlist)-rowMaxlist.__len__()
    to_be_fixed = baseMDF[(baseM==0) & (baseMDF!=0)].fillna(0.0)
    base = df.sum().sum() - baseMDF.sum().sum() - to_add
    print int(base - baseMDF[(baseM==0) & (baseMDF!=0)].fillna(0.0).sum().sum() + 2*np.count_nonzero(to_be_fixed))
    str = raw_input('max col number and row number:')

