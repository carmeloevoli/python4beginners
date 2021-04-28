### Lesson 11 - matplotlib basics
import matplotlib
matplotlib.use('MacOSX')

import matplotlib.pyplot as plt

import numpy as np
from scipy import fftpack

np.random.seed(1234)

time_step = 0.02
period = 5.

time_vec = np.arange(0, 20, time_step)
sig = (np.sin(2 * np.pi / period * time_vec)
       + 0.5 * np.random.randn(time_vec.size))

plt.figure(figsize=(6, 5))
plt.plot(time_vec, sig, label='Original signal')

https://scipy-lectures.org/intro/scipy/auto_examples/plot_fftpack.html

https://matplotlib.org/stable/gallery/index.html

#plt.plot([1,2,3,4],[1,4,9,16])
#plt.title('first plot')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.show()

#plt.figure(figsize=(15,5))
#plt.plot([1,2,3,4],[1,4,9,16])
#plt.show()

fig, ax = plt.figure(figsize=([15,5]))
