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

# x = ["Linear Hash","Extendiable Hash","B+ tree"]
# y1 = [4937,2102,8249]
# plt.plot(x, y1,color="red", linewidth=2.5, linestyle="-", label="Select")

x = ["1","2","3","4"]
y1 = [0.65,0.66,0.74,0.76]
plt.plot(x, y1,color="red", linewidth=2.5, linestyle="-", label="第一种")

x = ["1","2","3","4"]
y1 = [0.66,0.68,0.70,0.71]
plt.plot(x, y1,color="blue", linewidth=2.5, linestyle="-", label="第二种")


x = ["1","2","3","4"]
y1 = [0.68,0.733,0.766,0.793]
plt.plot(x, y1,color="green", linewidth=2.5, linestyle="-", label="第三种")
# x = ["Linear Hash","Extendiable Hash","B+ tree"]
# y1 = [3527,2758,24662]
# plt.plot(x, y1,color="blue", linewidth=2.5, linestyle="-", label="Modify")


# x = ["Linear Hash","Extendiable Hash","B+ tree"]
# y1 = [27152,29673,20458]
# plt.plot(x, y1,color="green", linewidth=2.5, linestyle="-", label="Remove")

#plt.figure(1)
#plt.subplot(111)

# plt.plot(x, y1,color="blue", linewidth=2.5, linestyle="-", label="XGBOOST")

#plt.subplot(212)
#设置x轴范围
#xlim(-2.5, 2.5)
#设置y轴范围

plt.xlabel('x轴')
plt.ylabel('胜率')

legend(loc='upper left')
plt.show()