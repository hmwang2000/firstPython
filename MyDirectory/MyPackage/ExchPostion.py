'''
交换位置
题目 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
程序分析 无
'''

list=[3,2,5,7,8,1,5]

print("Max list: ", max(list))
print("Min list: ", min(list))

print("Max list index: ", list.index(max(list)))
print("Min list index: ", list.index(min(list)))


list[-1],list[list.index(min(list))]=list[list.index(min(list))],list[-1]
m=list[0]
ind=list.index(max(list))

list[0]=list[ind]

list[ind]=m
print(list)
