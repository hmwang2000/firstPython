import numpy as np

a = np.arange(8)
print('原始数组：')
print(a)
print('\n')

b = a.reshape(4, 2)
print('修改后的数组：')
print(b)

#numpy.ndarray.flat 是一个数组元素迭代器
a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)

#numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下
#ndarray.flatten(order='C')
#参数说明：
#    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
a = np.arange(8).reshape(2, 4)
print('原数组：')
print(a)
print('\n')
# 默认按行

print('展开的数组：')
print(a.flatten())
print('\n')

print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))

a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')

print('对换数组：')
print(np.transpose(a))

#numpy.ndarray.T 类似 numpy.transpose
print ('转置数组：')
print (a.T)

'''
numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
numpy.rollaxis(arr, axis, start)
参数说明：
    arr：数组
    axis：要向后滚动的轴，其它轴的相对位置不会改变
    start：默认为零，表示完整的滚动。会滚动到特定位置。
'''
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('\n')
# 将轴 2 滚动到轴 0（宽度到深度）

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2))
# 将轴 0 滚动到轴 1：（宽度到高度）
print('\n')

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2, 1))

'''
numpy.swapaxes 函数用于交换数组的两个轴，格式如下：
numpy.swapaxes(arr, axis1, axis2)
    arr：输入的数组
    axis1：对应第一个轴的整数
    axis2：对应第二个轴的整数
'''
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）

print('调用 swapaxes 函数后的数组：')
print(np.swapaxes(a, 2, 0))

print("---------------------------修改数组维度---------------------------------")
'''
numpy.squeeze 函数从给定数组的形状中删除一维的条目，函数格式如下：
numpy.squeeze(arr, axis)
参数说明：
    arr：输入数组
    axis：整数或整数元组，用于选择形状中一维条目的子集
'''
print("---------------------------squeeze---------------------------------")

x = np.arange(9).reshape(1, 3, 3)

print('数组 x：')
print(x)
print('\n')
y = np.squeeze(x)

print('数组 y：')
print(y)
print('\n')

print('数组 x 和 y 的形状：')
print(x.shape, y.shape)


'''
numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状，函数格式如下:
 numpy.expand_dims(arr, axis)
参数说明：
    arr：输入数组
    axis：新轴插入的位置
'''
print("---------------------------expand_dims---------------------------------")

x = np.array(([1, 2], [3, 4]))

print('数组 x：')
print(x)
print('\n')
y = np.expand_dims(x, axis=0)

print('数组 y：')
print(y)
print('\n')

print('数组 x 和 y 的形状：')
print(x.shape, y.shape)
print('\n')
# 在位置 1 插入轴
y = np.expand_dims(x, axis=1)

print('在位置 1 插入轴之后的数组 y：')
print(y)
print('\n')

print('x.ndim 和 y.ndim：')
print(x.ndim, y.ndim)
print('\n')

print('x.shape 和 y.shape：')
print(x.shape, y.shape)

'''
numpy.broadcast
numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
该函数使用两个数组作为输入参数
'''
print("---------------------------numpy.broadcast---------------------------------")

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

# 对 y 广播 x
b = np.broadcast(x, y)
# 它拥有 iterator 属性，基于自身组件的迭代器元组

print('对 y 广播 x：')
r, c = b.iters

# Python3.x 为 next(context) ，Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))
print('\n')
# shape 属性返回广播对象的形状

print('广播对象的形状：')
print(b.shape)
print('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x, y)
c = np.empty(b.shape)

print('手动使用 broadcast 将 x 与 y 相加：')
print(c.shape)
print('\n')
c.flat = [u + v for (u, v) in b]

print('调用 flat 函数：')
print(c)
print('\n')
# 获得了和 NumPy 内建的广播支持相同的结果

print('x 与 y 的和：')
print(x + y)

'''
numpy.broadcast_to
numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。 
如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError
'''
print("---------------------------numpy.broadcast_to---------------------------------")
a = np.arange(4).reshape(1, 4)

print('原数组：')
print(a)
print('\n')

print('调用 broadcast_to 函数之后：')
print(np.broadcast_to(a, (4, 4)))

'''
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
该函数接收两个参数：
numpy.ravel(a, order='C')
参数说明：
    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序
'''
print("---------------------------numpy.ravel---------------------------------")
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))


