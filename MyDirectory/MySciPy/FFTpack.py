'''
对时域信号计算傅里叶变换以检查其在频域中的行为。 傅里叶变换可用于信号和噪声处理，图像处理，音频信号处理等领域。
SciPy提供fftpack模块，可让用户计算快速傅立叶变换。
'''

#Importing the fft and inverse fft functions from fftpackage
from scipy import fftpack
from scipy.fftpack import fft
from scipy.fftpack import ifft
import numpy as np

print("---------------------一维离散傅立叶变换-----------------------")
#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#长度为N的序列x [n]的FFT y [k]由fft()计算，逆变换使用ifft()计算
#Applying the fft function
y = fft(x)
print (y)

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
#FFT is already in the workspace, using the same workspace to for inverse transform

yinv = ifft(y)

print (yinv)


print("-----以0.02秒的时间步长创建一个信号,sig.size显示信号sig的大小-----")
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 *np.random.randn(time_vec.size)
print (sig.size)
#scipy.fftpack.fftfreq()函数将生成采样频率，scipy.fftpack.fft()将计算快速傅里叶变换
sample_freq = fftpack.fftfreq(sig.size, d = time_step)
sig_fft = fftpack.fft(sig)
print (sig_fft)


print("---------------------离散余弦变换----------------------------")

from scipy.fftpack import dct
from scipy.fftpack import idct

mydict = dct(np.array([4., 3., 5., 10., 5., 3.]))
print(mydict)

d = idct(np.array([4., 3., 5., 10., 5., 3.]))
print(d)

