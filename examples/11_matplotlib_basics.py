### Lesson 11 - matplotlib basics
### Gallery: https://matplotlib.org/stable/gallery/index.html

import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

import numpy as np

np.random.seed(1234)

def read_signal(time_step, period):
    time = np.arange(0, 20, time_step)
    noise = 0.5 * np.random.randn(time.size)
    sig = np.sin(2 * np.pi / period * time) + noise
    return time, sig

def filter_signal(time, sig):
    from scipy import fftpack
    sig_fft = fftpack.fft(sig)
    power = np.abs(sig_fft)**2

    sample_freq = fftpack.fftfreq(sig.size, d=time_step)

    pos_mask = np.where(sample_freq > 0)
    freqs = sample_freq[pos_mask]
    peak_freq = freqs[power[pos_mask].argmax()]

    high_freq_fft = sig_fft.copy()
    high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
    filtered_sig = fftpack.ifft(high_freq_fft)
    
    return filtered_sig

# THE PLOT

time_step = 0.02
period = 5.0

time, signal = read_signal(time_step, period)
filtered_signal = filter_signal(time, signal)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111)

ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude')

ax.plot(time, signal, label='Original signal', linewidth=2, color='blue', linestyle='-')
ax.plot(time, filtered_signal, label='Filtered signal', linewidth=3, color='red', linestyle=':')

ax.text(1, -2, 'FFT', fontsize=20)

ax.legend(loc='best')

#plt.show()
plt.savefig('FFT.pdf')
