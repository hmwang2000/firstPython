# !/usr/bin/python3

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

print ("第三个元素为 : ", list1[2])
list1[2] = 2018
print ("更新后的第三个元素为 : ", list1[2])

print ("原始列表 : ", list1)
del list1[2]
print ("删除第三个元素 : ", list1)

list3=[3*x for x in list2]
print ("列表推导式 : ", list3)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("x=",x)
print("x[0]=",x[0])
print("x[0][1]=",x[0][1])

list2.append(2)
print(list2.count(2))

list3=[7,8,9]
list2.extend(list3)
print("list2=",list2)

list2.pop()
print("list2=",list2)

list2.pop()
print("list2=",list2)


aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("列表元素 : ", list1)

str="Hello World"
list2=list(str)
print ("列表元素list2 : ", list2)
list2.reverse()
print ("反转列表元素list2 : ", list2)

list3=list2.copy()
list3.sort()
print ("排序列表元素list3 : ", list3)
