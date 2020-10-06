import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

# print(np.__version__) the version string is stored under __version__ attribute.

# print(type(arr))
# ..... type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.


arr_two = np.array([[1,2],[3,4]])
print(arr_two)


arr_three = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_three)


arr_x = np.array([1, 2, 3, 4], ndmin=5) #5 boyutlu dizi
print(arr_x)
print('number of dimensions :', arr_x.ndim)


arr_y = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr_y[0, 1])

arr_z = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr_z[1, -1]) #10 basar