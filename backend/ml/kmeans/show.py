# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

x = [10,20,40,80,160]
y1 = [7.448,7.537,7.602,7.684,7.725]
plt.plot(x, y1,color="red", linewidth=2.5, linestyle="-", label="MCMC")

x = [10,20,40,80,160]
y1 = [7.11,7.3,7.519,7.611,7.658]

#plt.figure(1)
#plt.subplot(111)

plt.plot(x, y1,color="blue", linewidth=2.5, linestyle="-", label="ALS")

#plt.subplot(212)
#设置x轴范围
#xlim(-2.5, 2.5)
#设置y轴范围

x = [10,20,40,80,160]
y1 = [7.08,7.074,7.05,7.043,7.068]
plt.plot(x, y1,color="black", linewidth=2.5, linestyle="-", label="SGD")

plt.xlabel('样本/万')
plt.ylabel('评估值')
ylim(6.8, 7.8)
legend(loc='upper left')
plt.grid(True)
plt.show()