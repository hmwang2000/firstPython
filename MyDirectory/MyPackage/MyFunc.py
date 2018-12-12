'''
Python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
    比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la
    也会受影响

Python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

#传不可变对象实例
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)  # 结果是 2

#传可变对象实例
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

#函数参数的使用不需要使用指定顺序
def printinfo1(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return

# 调用printinfo函数
printinfo1(age=50, name="David")

#调用函数时，如果没有传递参数，则会使用默认参数
def printinfo2(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return

# 调用printinfo函数
printinfo2(age=50, name="George")
print("------------------------")
printinfo2(name="George")

'''
不定长参数

可能需要一个函数能处理比当初声明时更多的参数。
这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。

基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]

加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
如果在函数调用时没有指定参数，它就是一个空元组。
'''
def printinfo3(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)

# 调用printinfo 函数
printinfo3(70, 60, 50)

'''
还有一种就是参数带两个星号 **基本语法如下：
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了两个星号 ** 的参数会以字典的形式导入。
'''
def printinfo4(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo4(1, a=2, b=3)
