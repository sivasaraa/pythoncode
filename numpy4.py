import numpy as np

list1 = [0,1,2,3,4,5]
arr = np.array(list1)
print(arr)
print(type(arr))

# 2d array
arr1 = np.array([[1,2,3],[3,4,5],[5,6,7]])
print(arr1)
print(arr1.ndim)

# float array
arr2 = np.array(list1, dtype='float')
print(arr2)

# float into int
print(arr2.astype('int'))

# array to list
print(arr2.astype('int').tolist())

print("dimensional",arr.ndim)
print("nrow and ncol",arr.shape)
print("datatype",arr.dtype)
print("no of items",arr.size)

# reverse the arr1
print(arr1[::-1])

# min max and mean
print("min",arr1.min())
print("max",arr1.max())
print("mean",arr1.mean())

# row and column wise
print("row wise",np.amin(arr1,axis=1))
print("col wise",np.amin(arr1,axis=0))

# reshaping
arr3 = np.array([[1,2],[3,4],[5,6]])
print(arr3.reshape(2,3))

# sequence repeat and random
ax = np.arange(4)
print("range",ax)

ax = np.tile(ax,2)
print(ax)

ax = np.repeat(ax,2)
print(ax)

# if num of element is known
ax = np.linspace(20,50,5,dtype='int')
print(ax)

#random number between 0 to 1
print(np.random.rand())

print(np.random.randint(1,10,(3,3)))

#choice
print(np.random.choice(['a','b','c','d','e'],10))

# get same random number
np.random.seed(50)
print(np.random.randint(1,16,(2,3)))

# get unique numbers and count
cc = np.random.randint(1,10,10)
print(cc)
uniq,count = np.unique(cc,return_counts=True)
print("unique",uniq)
print("count",count)