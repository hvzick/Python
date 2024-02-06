import numpy as np

# addition on 2D array
a1 = np.array([(1, 2, 3), (2, 5, 8)])
a2 = np.array([(3, 7, 7), (9, 3, 6)])
sum1 = a1 + a2
print(sum1)

# to check dimension of an array
print(a1.ndim)

# size of array
print(sum1.size)

# to check rows and columns of array
print(sum1.shape)

# to reshape our array
print(a1)  # before
print(a1.reshape(3, 2))  # after

print(sum1.max())
print(sum1.min())

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = np.array(arr1)
print(r)

print(r.sum(axis=1))
# [1, 2, 3] = 6
# [4, 5, 6] = 15
# [7, 8, 9] = 24

print(r.sum(axis=0))

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# 12  15  18

print(r.T)

# [1, 2, 3],      [1, 4, 7],
# [4, 5, 6],  to  [2, 5, 8],
# [7, 8, 9]       [3, 6, 9]


# for item in r.flat:
#     print(item)

print(r.ndim)
print(r.nbytes)

# gives index of min value in the array
one = np.array([4, 64, 5, 3, 2, 7])
print(one.argmin())

# gives index of max value in the array
print(one.argmax())

# give us how our indicies should be to sort the array
print(one.argsort())

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9] max here
print(r.argmax(axis=1))
print(r.argmin(axis=0))

a = [[6, 3], [5, 4]]
b = [[7, 1], [9, 2]]
ar = np.array(a)
br = np.array(b)

# print(ar + br)
# print(ar * br)
# print(ar - br)
# print(ar / br)

print(np.where(ar > 5))
print(np.count_nonzero(ar))
print(np.nonzero(ar))

import sys

print(sys.getsizeof(1) * len(a))
print(ar.itemsize * ar.size)