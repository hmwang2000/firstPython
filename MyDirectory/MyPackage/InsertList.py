'''
有序列表插入元素
题目 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
程序分析 首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''

a=[1,100,10000]
b=[10,1000,1000000]
a.extend(b)
a.sort()
print(a)

lis=[1,10,100,1000,10000,100000]
#n=int(input('insert a number: '))
n=123
lis.append(n)

for i in range(len(lis)-1):
    if lis[i]>=n:
        print(i)
        for j in range(i,len(lis)-1):
            lis[j],lis[-1]=lis[-1],lis[j]
            print(lis)
        break

print(lis)
