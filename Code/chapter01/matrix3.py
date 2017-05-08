# -*- coding: utf-8 -*-

import sys  
import os
import time
from numpy import *
import imp

# 配置utf-8输出环境
imp.reload(sys)
sys.setdefaultencoding('utf-8')

mymatrix = mat([[1,2,3],[4,5,6],[7,8,9]])

mymatrix2 = mat([[1],[2],[3]])
print(mymatrix*mymatrix2)

# 矩阵的转置
print(mymatrix.T)
mymatrix.transpose()
print(mymatrix)