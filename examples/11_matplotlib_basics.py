### Lesson 11 - matplotlib basics
import matplotlib
matplotlib.use('MacOSX')

import matplotlib.pyplot as plt

#plt.plot([1,2,3,4],[1,4,9,16])
#plt.title('first plot')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.show()

#plt.figure(figsize=(15,5))
#plt.plot([1,2,3,4],[1,4,9,16])
#plt.show()

fig, ax = plt.figure(figsize=([15,5]))
