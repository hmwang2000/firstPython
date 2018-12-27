import numpy as np

a = np.array([1,2,3])
print(a)

a = np.array([[1,  2],  [3,  4]])
print (a)

a = np.array([1,2,3,4,5], ndmin =  2)
print (a)

a = np.array([1,  2,  3], dtype = complex)
print (a)

a = np.array([1,  2,  3], dtype = complex, ndmin = 2)
print (a)

# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

# 字节顺序标注
dt = np.dtype('>i4')
print(dt)

# 使用标量类型
# dt = np.dtype([('age',np.int8)])
print(dt)


# 将数据类型应用于 ndarray 对象
dt = np.dtype([('age',np.int8)])
print(dt)
a = np.array([(10),(20),(30)], dtype = dt)
print(a)
print(a['age'])

#下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 adarray 对象
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)
print(a['name'],a['age'],a['marks'])


a = np.arange(24)
print(a.ndim)             # a 现只有一个维度
print(a)
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)
print(b)

a = np.array([[1,2,3],[4,5,6]])
print (a.shape)

#调整数组大小
a = np.array([[1,2,3],[4,5,6]])
a.shape =  (3,2)
print (a)

#NumPy 也提供了 reshape 函数来调整数组大小
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print (b)

'''
ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
例如，一个元素类型为 float64 的数组 itemsiz 属性值为 8(float64 占用 64 个 bits，
每个字节长度为 8，所以 64/8，占用 8 个字节），又如，一个元素类型为 complex32 的数组 item 属性为 4（32/8）
'''
# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)

#ndarray.flags 返回 ndarray 对象的内存信息
x = np.array([1,2,3,4,5])
print (x.flags)