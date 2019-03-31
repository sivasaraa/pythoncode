import numpy as np

# Basic operation

a = np.array([1,2,3])
print("dimension",a.ndim)

a = np.array([[1,2],[3,4]])
print("dimension",a.ndim)  # dimension of a

print("size",a.itemsize) # individual size of element

print("datatype",a.dtype)  # datatype of np array

a = np.array([1,2,3], dtype=np.float)
print("float size",a.itemsize)
print("datatype",a.dtype)

a = np.array([[1,2],[2,3],[3,4]])
print("row x col",a.shape)

# default values
a = np.zeros((3,2), dtype=np.int)
print("zeros",a)

a = np.ones((3,2), dtype=np.int)
print("ones",a)

# Range
a = np.arange(5)
print(a)

# Linear space
a = np.linspace(1,5,10)
print(a)

a = np.linspace(1,5,10 ,endpoint = False)
print("without endpoint",a)

# Reshape
a = np.array([[1,2],[2,3],[3,4]])
print(a)

a = a.reshape(2,3)
print("after reshape",a)

# flatten as 1 dimension array
a = np.ravel(a)
print(a)

a = a.reshape(3,2)
print(a)
print("min",a.min())
print("max",a.max())
print("sum",a.sum())
print("sum axis 0(col)",a.sum(axis = 0))
print("sum axis 1(row)",a.sum(axis = 1))
print("square root",np.sqrt(a))
print("sd",a.std())
