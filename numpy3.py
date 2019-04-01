import numpy as np

a = np.array([[1,2,3],[6,7,8],[9,3,2]])
print(a)

# indexing
print("indexing1",a[0:2,2])
print("last row",a[-1])

# iterate
print("row wise")
for row in a:
    print(row)

print("individual element")
for row in a:
    for e in row:
        print(e)

# flattern
print("flattern")
for cell in a.flat:
    print(cell)

# horizontal and vertical stack
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print("horizontal stack")
print(np.hstack((a,b)))
print("vertical stack")
print(np.vstack((a,b)))

# split
print("splitting")
a = np.arange(16).reshape((4,4))
result = np.hsplit(a,2)
print(result)