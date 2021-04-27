# numpy tutorial
# numpy is optmized for array and data handling, written in C

# 1. installation
#
# pip install numpy
# or
# conda install numpy

import numpy as np
print(np.__version__)

# 2. NumPy array

a = np.array([1,2,3,4,5])

print (a.shape)
print (a.dtype)
print (a.ndim)
print (a.size)
print (a.itemsize) # the size in byte of each element

a = np.array([1,2,3,4,5], dtype=np.int64)
print (a.dtype, a.itemsize)

a = np.array([1,2,3,4,5], dtype=np.float32)
print (a.dtype, a.itemsize)

# 2.1 access

print (a[0])
a[1] = 7
print (a)

# 2.2 elementwise operations

b = np.array([6,7,8,9,10])
print (a + b)
print (a * b)

c = a * b
print (c.sum())

# 3. NumPy vs Lists

l = [1,2,3]
v = np.array([1,2,3])

print (2 * l)
print (2 * v) # all operations are applied at each element

# 4. Dot product

v1 = np.array([1, 4, 3])
v2 = np.array([5, 2, 7])

dot = 0
for i in range(len(v1)):
    dot += v1[i] * v2[i]
print (dot)

dot = np.dot(v1,v2) # as a function of two arrays
print (dot)

dot = v1.dot(v2) # as an instance method
print (dot)

dot = v1 @ v2
print (dot)

# 4.1 Speed test comparison

from timeit import default_timer as timer
a = np.random.randn(1000)
b = np.random.randn(1000)
A = list(a)
B = list(b)
T = 1000

def dot1():
    dot = 0
    for i in range(len(a)):
        dot += A[i] * B[i]
    return dot
    
def dot2():
    return np.dot(a,b)

start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end - start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end - start

print(t1)
print(t2)
print(t1/t2)

# 5. Multidimensional array

a = np.array([[1,2], [3,4]]) # 2D matrix (not forget the double square brackets!)
print (a)
print (a.shape)

# 5.1 access elements

print (a[0])
print (a[0][0])
# or
print (a[0,0])

# 5.2 slicing

print (a[:,0])
print (a[0,:])

# 5.3 transpose

print (a.T)

# 5.4 matrix multiplication

print (a * a)

b = [[1,2,3], [4,5,6]]
print (a.dot(b)) # (2 x 2) \dot (2 x 3)

# 5.5 simple algebric operations

c = np.linalg.det(a) # determinant
print (c)
c = np.linalg.inv(a) # inverse
print (c)
c = np.diag(a) # take only the diagonal part
print (c)

# 6. Indexing and slicing

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[0,1]
print(b)

row0 = a[0,:]
print (row0)

col0 = a[:, 0]
print (col0)

slice_0 = a[2:3,1:2]
print (slice_0)

last_element = a[-1,-1]
print (last_element)

# 6.1 boolean indexing

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

bool_idx = a > 2
print(bool_idx)

b = a[bool_idx]
print(b) # notice that is a 1-D vector

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[a > 2])

# np.where()
# Return elements chosen from x depending on condition
b = np.where(a > 2, a, -1)
print(b)

# np.argwhere()
# Find the indices of array elements that are non-zero, grouped by element
a = np.array([10,19,32,21,27,33,40])

b = a[[2,4,6]] # use list index
print(b)

even = np.argwhere(a % 2 == 0).flatten()
print(even)
print(a[even])

# 7. reshape

a = np.arange(1,7)
print(a)

b = a.reshape(2,3)
print(b)

b = a.reshape(3,2)
print(b)

# 7.1 newaxis

print(a.shape)

d = a[np.newaxis,:]
print(d)
print(d.shape)
print(d is a)

# 8. broadcasting

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b = np.array([0,1,2])

print (a + b)

# 9. functions and axis

a = np.array([[7,8,9,10,11,12,13,14],[15,16,17,18,19,20,21,22]])
print (a.sum())
print (a.sum(axis=None))
print (a.sum(axis=0))
print (a.sum(axis=1))

print (a.mean())
print (a.std())
print (a.min())
print (a.max())

# 10. copying

a = np.array([1,2,3])
b = a # pointer!
b[0] = -100
print(a)

a = np.array([1,2,3])
b = a.copy()
b[0] = -100
print(a)

# 11. generating arrays

a = np.zeros((2,3)) # <- tuple
print(a)

b = np.ones((2,3))
print(b)

c = np.full((2,3), 5.0)
print(c)

d = np.eye(4) # identity!
print(d)

e = np.arange(10)
print(e)

f = np.linspace(0, 100, 5)
print(f)

g = np.logspace(-1, 2, 10)
print(g)

print(2. * np.power(g, -2.7))

# 12. Linear algebra

a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors) # !column vectors

eigenvector_0 = eigenvectors[:,0]

print(eigenvector_0)

# 12.1 solving lineary systems

A = np.array([[1, 1], [1.5, 4.]])
b = np.array([2200, 5500])
# Ax = b -> x = A^-1 * b

x = np.linalg.inv(A).dot(b)
print(x)

x = np.linalg.solve(A,b) # faster!
print(x)

# 13. load file

x, y = np.loadtxt("demofile.txt", usecols=(0,1), unpack=True, skiprows=1) #, delimiter=',', dtype=np.float32)
print (y)

np.save("savefile", x)

# 14. random routines

predictions = np.random.randn(1000)
measurements = np.random.randn(1000)
assert(len(predictions) == len(measurements))
chi2 = (1. / len(predictions)) * np.sum(np.square(predictions - measurements))
print (chi2)

from scipy.stats import chi2
prob = 0.95
dof = 100
print (chi2.ppf(prob, dof) / (dof - 1))
