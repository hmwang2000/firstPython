import numpy as np
from numpy import random

#numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
x = np.empty([3,2], dtype = int)
print (x)

# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

# 默认为浮点数
x = np.ones(5)
print(x)

# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)

# 创建 randn(size) 服从 X~N(0,1) 的正态分布随机数组
a=random.randn(2,3)
print(a)

a=random.randint(100,200,(3,3))
print(a)
