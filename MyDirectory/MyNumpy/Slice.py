import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)

# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])

print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素


print("---------整数数组索引---------")
#以下实例获取数组中(0,0)，(1,1)和(2,0)位置处的元素。
x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x)
y = x[[0,1,2],  [0,1,0]]
print (y)

print("----以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]----")
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
print("rows=",rows)
print("cols=",cols)
y = x[rows,cols]
y = x[rows,cols]
print('这个数组的四个角元素是：')
print (y)

#切片 : 或 … 与索引数组组合
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print("b=",b)
print("c=",c)
print("d=",d)

print("------------布尔索引------------")
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素
print  ('大于 5 的元素是：')
print (x[x >  5])


#使用了 ~（取补运算符）来过滤 NaN
a = np.array([np.nan,  1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])

#从数组中过滤掉非复数元素
a = np.array([1,  2+6j,  5,  3.5+5j])
print (a[np.iscomplex(a)])

print("----------花式索引----------")
'''
花式索引指的是利用整数数组进行索引。
花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。
对于使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应位置的元素；
如果目标是二维数组，那么就是对应下标的行。
花式索引跟切片不一样，它总是将数据复制到新数组中。
'''
x=np.arange(32).reshape((8,4))
print(x)
print("\n")
print (x[[4,2,1,7]])
print("\n")

x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])
print("\n")

x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
print("\n")

