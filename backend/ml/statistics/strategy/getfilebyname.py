# -*- coding: utf-8 -*-

import os
import pandas as pd

file = pd.read_csv("select200.csv")

for f in file['name']:
    os.system("cp ../../../fixeddata/"+str(f).zfill(6)+".csv"+" ../../../200/")