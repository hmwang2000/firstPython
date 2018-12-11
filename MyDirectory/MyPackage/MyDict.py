# !/usr/bin/python3

'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

d = {key1 : value1, key2 : value2 }

键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}  #创建字典

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict['Age'] = 8;  # 更新 Age
dict['School'] = "北大附中"  # 添加信息

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典

dict = {'Name': 'Heather', 'Age': 7, 'Class': 'First'}  #创建字典
dict['Age'] = 16;  # 更新 Age
dict['School'] = "Whittman"  # 添加信息
try:
    print("dict['Age']: ", dict['Age'])
    print("dict['School']: ", dict['School'])
except TypeError:
    print("TypeError: Not found")
except:
    print("Other Error")
else:
    print("Else Statement")


print(len(dict))
print(str(dict))
print(type(dict))

print(dict.keys())
print(list(dict.keys()))
print(dict.values())
print(list(dict.values()))

print("Value : %s" %  dict.items())

dict.popitem()
print(list(dict.values()))
