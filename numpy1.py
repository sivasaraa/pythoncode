import numpy as np
import sys
import time


#comparing the memory of list and numpy array
# 1 memory
list1 = range(1000)
print(sys.getsizeof(1)*len(list1)) #size of list1[1]

arr1 = np.arange(1000)
print(arr1.size*arr1.itemsize) #total array length and one array size(item size)

# 2 performance

l1 = range(100000)
l2 = range(100000)
start = time.time()
[(x+y) for x,y in zip(l1,l2)]
print("list time",time.time()-start)

a1 = np.arange(10000)
a2 = np.arange(10000)
start = time.time()
a1+a2
print("numpy time",time.time()-start)
