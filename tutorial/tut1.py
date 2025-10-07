import numpy as np

# creating array from list
arr_1d=np.array([1,2,3,4,5])
print("one-d array:",arr_1d)
arr_2d=np.array([[1,2,3],[4,5,6]])
print("two-d array:",arr_2d)
# data types similar for fast ops

# diff between list and numpy array
py_list=[1,2,3]
print("py_list multipliction:",py_list*2)
numpy_array=np.array([1,2,3])#element wise multiplication
print("numpy_array multipliction:",numpy_array*2)

# creating array from scratch
zeroes=np.zeros((3,4))
print("zeroes:",zeroes)
ones=np.ones((3,4))
print("ones:",ones)
full=np.full((2,2),7)
print("full:",full)
random=np.random.random((2,3))
print("random:",random)
sequence=np.arange(0,10,2)#range non inclusive boundry give 10 only goes till 9
print("sequence:",sequence)

# vector,matrix,tensor
vector=np.array([1,2,3])
print("vector:",vector)
matrix=np.array([[1,2],[3,4]])
print("matrix:",matrix)
tensor=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("tensor:",tensor)

# array properties
arr=np.array([[1,2,3],[4,5,6]]) #true 6.8,'6.8'
print("shape:",arr.shape)
print("ndim:",arr.ndim)
print("size:",arr.size)
print("dtype:",arr.dtype)#type converstion?

# array reshaping
arr=np.arange(12)
print('arr:',arr)
reshaped=arr.reshape((3,4))
print('reshape:',reshaped)
flat=reshaped.flatten()
print('flat:',flat)
ravelled=reshaped.ravel()
print('ravelled:',ravelled)
transpose=reshaped.transpose()
print('transposed:',transpose)
# ravel,flat??