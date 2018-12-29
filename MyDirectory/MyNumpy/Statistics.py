import numpy as np

print("-------------------numpy.numpy.amin() 和 numpy.amax()----------------------")
#numpy.amin() 用于计算数组中的元素沿指定轴的最小值。
# numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 amin() 函数：')
print (np.amin(a,1))
print ('\n')
print ('再次调用 amin() 函数：')
print (np.amin(a,0))
print ('\n')
print ('调用 amax() 函数：')
print (np.amax(a))
print ('\n')
print ('再次调用 amax() 函数：')
print (np.amax(a, axis =  0))

print("-------------------numpy.ptp()----------------------")
#numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）。
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 ptp() 函数：')
print (np.ptp(a))
print ('\n')
print ('沿轴 1 调用 ptp() 函数：')
print (np.ptp(a, axis =  1))
print ('\n')
print ('沿轴 0 调用 ptp() 函数：')
print (np.ptp(a, axis =  0))

print("-------------------numpy.percentile()----------------------")
#百分位数是统计中使用的度量，表示小于这个值的观察值的百分比

a = np.array([[10, 9, 8, 7], [4, 3, 2, 1]])
print('我们的数组是：')
print(a)

print('调用 percentile() 函数：')
# 50% 的分位数，就是 a 里排序之后的中位数
print(np.percentile(a, 50))

# axis 为 0，在纵列上求
print(np.percentile(a, 50, axis=0))

# axis 为 1，在横行上求
print(np.percentile(a, 50, axis=1))

# 保持维度不变
print(np.percentile(a, 50, axis=1, keepdims=True))

print("-------------------numpy.median()----------------------")
#numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 median() 函数：')
print (np.median(a))
print ('\n')
print ('沿轴 0 调用 median() 函数：')
print (np.median(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 median() 函数：')
print (np.median(a, axis =  1))

print("-------------------numpy.mean()----------------------")
#numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 mean() 函数：')
print (np.mean(a))
print ('\n')
print ('沿轴 0 调用 mean() 函数：')
print (np.mean(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 mean() 函数：')
print (np.mean(a, axis =  1))

print("-------------------numpy.mean()----------------------")
#numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
a = np.array([1,2,3,4])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 average() 函数：')
print (np.average(a))
print ('\n')
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])
print ('再次调用 average() 函数：')
print (np.average(a,weights = wts))
print ('\n')
# 如果 returned 参数设为 true，则返回权重的和
print ('权重的和：')
print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))

print("-------------------numpy.std()----------------------")
#标准差
#标准差是一组数据平均值分散程度的一种度量。
#标准差是方差的算术平方根。
#标准差公式如下：std = sqrt(mean((x - x.mean())**2))
print (np.std([1,2,3,4]))

print("-------------------numpy.var()----------------------")
#方差
#统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean((x - x.mean())** 2)。
#换句话说，标准差是方差的平方根。
print (np.var([1,2,3,4]))