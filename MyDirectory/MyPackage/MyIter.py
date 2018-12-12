# !/usr/bin/python3
# -*- coding: UTF-8 -*-

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

'''
创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
Python 的构造函数为 __init__(), 它会在对象初始化的时候执行
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置
在完成指定循环次数后触发 StopIteration 异常来结束迭代。
以下实例在 20 次迭代后停止执行
'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，返回一个 iterable 对象。在调用生成器运行的
过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。 
并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，
无需处理 StopIteration 异常，循环会正常结束。
以下实例使用 yield 实现斐波那契数列：
'''
import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

'''
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行
流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 
的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 
yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态
来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。

在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则
直接抛出 StopIteration 终止迭代。

如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断
'''
from inspect import isgeneratorfunction

bl = isgeneratorfunction(fibonacci)
print(bl)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

