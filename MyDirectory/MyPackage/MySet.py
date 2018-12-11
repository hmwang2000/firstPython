'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}
if 'orange' in basket:                 # 快速判断元素是否在集合内
    print ("orange in basket")
else:
    print ("orange NOT in basket")
if 'crabgrass' in basket:
    print ("crabgrass in basket")
else:
    print("crabgrass NOT in basket")


# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print("Set a=", a)
print("Set a-b=", a - b)                            # 集合a中包含而集合b中不包含的元素
print("Set a|b=", a|b)                              # 集合a或b中包含的所有元素
print("Set a&b=", a&b)                              # 集合a和b中都包含了的元素
print("Set a^b=", a^b)                              # 不同时包含于a和b的元素


x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.intersection(y)
print(z)

z = x.union(y)
print(z)

z = x.difference(y)
print(z)

#isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.isdisjoint(y)
print(z)

'''
添加元素
语法格式如下：
s.add( x )
将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
'''
thisset = set(("Google", "Oracle", "Microsoft"))
thisset.add("Facebook")
print(thisset)

thisset.discard("Oracle")
print(thisset)

thisset.remove("Google")
print(thisset)

'''
可以设置随机删除集合中的一个元素，语法格式如下：
s.pop() 
多次执行测试结果都不一样
然而在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）。 
'''
thisset = set(("Google", "Oracle", "Microsoft", "Facebook"))
print(len(thisset))
x = thisset.pop()
print(x)
