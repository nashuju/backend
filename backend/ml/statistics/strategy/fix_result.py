# -*- coding: utf-8 -*-

from src.db.File import File
import pandas as pd
import numpy as np

rs = File("../../../result")

file_paths = rs.get_file_names_without_suffix_in_current_dir()

templatefilepath = "../../../result/600089.csv"
template = pd.read_csv(templatefilepath)
template = template.sort_values(by = ['date','seqNo'],axis = 0,ascending = True)
firstday = template['date'][1]
endday   = firstday
for f in file_paths:
    fpath ="../../../result/"+ f+".csv"
    dt = pd.read_csv(fpath)
    if dt.shape[0] == 0: continue
    dt = dt.sort_values(by = ['date','seqNo'],axis = 0,ascending = True)
    dtfirstday = dt['date'][1]
    firstblock = dt.head(48)
    blank = dt.head(48)
    for date in template['date'].drop_duplicates():
        if dtfirstday > date:
            firstblock['date'] = date
            blank = blank.append(firstblock)
        elif dtfirstday < date:
            if date in np.array(dt['date'].drop_duplicates()):
                firstblock = dt[dt.date==date]
                firstblock['date'] = date
                blank = blank.append(firstblock)
            else:
                firstblock['date'] = date
                blank = blank.append(firstblock)
                pass

    blank.to_csv("../../../fixeddata/"+f+".csv",index=False,columns=["date","seqNo","open","close","high","low","volume","amount"])
    template = pd.read_csv(templatefilepath)
    pass