# !/usr/bin/python3

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print(tup3)

print("Max= ", max(tup1))
print("Min= ", min(tup1))

tuple1 = ('Google', 'Microsoft', 'Oracle')
print(tuple1*2)

list1= ['Google', 'Microsoft', 'Oracle', 'Amazon']
tuple2=tuple(list1)
print("List1=",list1, "Length=",len(list1))

print("Tuple2=",tuple2, "Length=",len(tuple2))

for x in tuple2:
    print(x)

for x in tuple2: print(x, end=";")

print()

print("tuple2[1]=",tuple2[1])
print("tuple2[-1]=",tuple2[-1])
print("tuple2[2:]=",tuple2[2:])

print(type(tuple2))

tup1 = (50)
print(type(tup1))  # 不加逗号，类型为整型

tup1 = (50,)
print(type(tup1))  # 加上逗号，类型为元组
