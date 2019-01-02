import numpy as np
from scipy.optimize import minimize

'''
scipy.optimize包提供了几种常用的优化算法。 该模块包含以下几个方面 -
    使用各种算法(例如BFGS，Nelder-Mead单纯形，牛顿共轭梯度，COBYLA或SLSQP)的无约束和约束最小化多元标量函数(minimize())
    全局(蛮力)优化程序(例如，anneal()，basinhopping())
    最小二乘最小化(leastsq())和曲线拟合(curve_fit())算法
    标量单变量函数最小化(minim_scalar())和根查找(newton())
    使用多种算法(例如，Powell，Levenberg-Marquardt混合或Newton-Krylov等大规模方法)的多元方程系统求解(root)
'''
print("--------------------Nelder–Mead单纯形算法------------------------")

print("--------------------最小二乘法------------------------")
def fun_rosenbrock(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

from scipy.optimize import least_squares
input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)

print (res)

print("--------------------求根------------------------")
from scipy.optimize import root
def func(x):
   return x*2 + 2 * np.cos(x)
sol = root(func, 0.3)
print (sol)
