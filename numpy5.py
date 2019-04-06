import numpy as np

# index using where condition
arr1 = np.random.randint(1,10,10)
print(arr1)
arr1_ind = np.where(arr1 > 5)
print("index",arr1_ind)
print("values",arr1[arr1_ind])

# location of max and min values
print("max index",arr1.argmax())
print("min index",arr1.argmin())

#load the csv file
np.set_printoptions(suppress=True)
path = 'https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data = np.genfromtxt(path,delimiter=',',skip_header=1,filling_values=-99,dtype=None)
print(data[:3])

#concatenate row and column wise of two array
a = np.zeros([3,4])
b = np.ones([3,4])
print("row",np.concatenate([a,b],axis=1))
print("column",np.concatenate([a,b],axis=0))

print(np.vstack([a,b]))
print(np.hstack([a,b]))

print(np.r_[a,b])
print(np.c_[a,b])

#sort numpy array
arr = np.random.randint(1,6,[8,4])
print("sort",np.sort(arr,axis=0))

# sort index
x = np.array([1, 10, 5, 2, 8, 9])
print("sort index",np.sort(x))

#column wise sorting
column_1_st = arr[:,0].argsort()
print(column_1_st)
print("first column sorted",arr[column_1_st])

# sort based on two columns
column_index = np.lexsort((arr[:,1],arr[:,0]))
print(column_index)
print(arr[column_index])

# vectorize scalar to vector

def foo(x):
    if x%2 == 1:
        return x**2
    else:
        return x/2

#scalar
print("pass x",foo(10))

# vector
foo_v = np.vectorize(foo)
print("pass vector x",foo_v([4,6,9]))

#apply_along_axis
def max_minus_min(x):
    return np.max(x) - np.min(x)

print('Row wise: ', np.apply_along_axis(max_minus_min, 1, arr))
print("column wise",np.apply_along_axis(max_minus_min,0,arr))


#histogram and bincount
x = np.array([1,1,2,2,2,4,4,5,6,6,6])
count,bin = np.histogram(x,[0,2,4,6,7])
print("count",count)
print("bin count",bin)

print("coursera questions")
arr1 = np.arange(36)[::7]
print(arr1)
arr2 = np.arange(36).reshape(6,6)
print(arr2[2:4,2:4])