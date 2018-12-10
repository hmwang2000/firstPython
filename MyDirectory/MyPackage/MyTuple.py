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
print("Tuple2=",tuple2, "Len=",len(tuple2))

for x in tuple2:
    print(x)

for x in tuple2: print(x)