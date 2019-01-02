'''
奇异值分解(SVD)可以被认为是特征值问题扩展到非矩阵的矩阵。
scipy.linalg.svd将矩阵'a'分解为两个酉矩阵'U'和'Vh'，以及一个奇异值(实数，非负)的一维数组's'，
使得a == U * S * Vh，其中'S'是具有主对角线's'的适当形状的零点矩阵。
'''

#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)

#Passing the values to the eig function
U, s, Vh = linalg.svd(a)

# printing the result
print (U, Vh, s)
