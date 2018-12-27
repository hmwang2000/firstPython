import numpy as np

'''
连接数组
函数 	        描述
concatenate 	连接沿现有轴的数组序列
stack 	        沿着新的轴加入一系列数组。
hstack 	        水平堆叠序列中的数组（列方向）
vstack 	        竖直堆叠序列中的数组（行方向）
'''
print("------------------------连接数组-----------------------")

print("------------------------numpy.concatenate------------------------")
#numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组
a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')
# 两个数组的维度相同

#axis：沿着它连接数组的轴，默认为 0
print('沿轴 0 连接两个数组：')
print(np.concatenate((a, b)))
print('\n')

print('沿轴 1 连接两个数组：')
print(np.concatenate((a, b), axis=1))

print("------------------------numpy.stack------------------------")
#numpy.stack 函数用于沿新轴连接数组序列

a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')

print('沿轴 0 堆叠两个数组：')
print(np.stack((a, b), 0))
print('\n')

print('沿轴 1 堆叠两个数组：')
print(np.stack((a, b), 1))


print("------------------------numpy.hstack------------------------")
#numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组

a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')

print('水平堆叠：')
c = np.hstack((a, b))
print(c)
print('\n')

print("------------------------numpy.vstack------------------------")
#numpy.hstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组

a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')

print('竖直堆叠：')
c = np.vstack((a, b))
print(c)

print("------------------------numpy.split------------------------")
#numpy.split 函数沿特定的轴将数组分割为子数组
a = np.arange(9)

print('第一个数组：')
print(a)
print('\n')

print('将数组分为三个大小相等的子数组：')
b = np.split(a, 3)
print(b)
print('\n')

print('将数组在一维数组中表明的位置分割：')
b = np.split(a, [4, 7])
print(b)

print("------------------------numpy.hsplit------------------------")
#numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组
harr = np.floor(10 * np.random.random((2, 6)))
print('原array：')
print(harr)

print('拆分后：')
print(np.hsplit(harr, 3))

print("------------------------numpy.vsplit------------------------")
#numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同
a = np.arange(16).reshape(4, 4)

print('第一个数组：')
print(a)
print('\n')

print('竖直分割：')
b = np.vsplit(a, 2)
print(b)

print("------------------------numpy.resize------------------------")
#numpy.resize 函数返回指定大小的新数组
#如果新数组大小大于原始大小，则包含原始数组中的元素的副本
a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('第一个数组的形状：')
print(a.shape)
print('\n')
b = np.resize(a, (3, 2))

print('第二个数组：')
print(b)
print('\n')

print('第二个数组的形状：')
print(b.shape)
print('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了

print('修改第二个数组的大小：')
b = np.resize(a, (3, 3))
print(b)


print("------------------------numpy.append------------------------")
#numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。
# 此外，输入数组的维度必须匹配否则将生成ValueError。
a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('向数组添加元素：')
print('未传递 Axis 参数, 输入数组会被展开。')
print(np.append(a, [7, 8, 9]))
print('\n')

print('沿轴 0 添加元素：')
print(np.append(a, [[7, 8, 9]], axis=0))
print('\n')

print('沿轴 1 添加元素：')
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

print("------------------------numpy.insert------------------------")
#numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值
a = np.array([[1, 2], [3, 4], [5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print('\n')
print('传递了 Axis 参数。 会广播值数组来配输入数组。')

print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print('\n')

print('沿轴 1 广播：')
print(np.insert(a, 1, 11, axis=1))

print("------------------------numpy.delete------------------------")
#numpy.delete 函数返回从输入数组中删除指定子数组的新数组。
# 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
a = np.arange(12).reshape(3, 4)

print('第一个数组：')
print(a)
print('\n')

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('\n')

print('删除第二列：')
print(np.delete(a, 1, axis=1))
print('\n')

print('包含从数组中删除的替代值的切片：')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))

print("------------------------numpy.unique------------------------")
#numpy.unique 函数用于去除数组中的重复元素
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

print('第一个数组：')
print(a)
print('\n')

print('第一个数组的去重值：')
u = np.unique(a)
print(u)
print('\n')

print('去重数组的索引数组（所剩元素在原数组的索引）：')
u, indices = np.unique(a, return_index=True)
print(indices)
print('\n')

print('我们可以看到每个和原数组下标对应的数值：')
print(a)
print('\n')

print('去重数组的下标：')
u, indices = np.unique(a, return_inverse=True)
print(u)
print('\n')

print('下标为：')
print(indices)
print('\n')

print('使用下标重构原数组：')
print(u[indices])
print('\n')

print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)


