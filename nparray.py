import numpy as np

arr1 = np.array([1,2,3,4,5])
print("1D Array", arr1)

# 2d array
arr2 = np.array([[1,2,3,4], [5,6,7,8]])
print("2d Array\n", arr2)

# using arrange(start, stop, step)
arr3 = np.arange(0,10,1)
print("Arranage array", arr3)

#using linspace()
arr4 = np.linspace(0,1,5)
print("Linspace Array:",arr4)

# special arrays
# arrays fo zeros
zero_arrays = np.zeros((2,3))
print("Zeros Array:\n", zero_arrays)

#Arrays of one
ones_array = np.ones((2,2))
print("Ones Array\n", ones_array)

# Empty array 
epaty_array = np.empty((3,3))
print("Empty Array\n",epaty_array)


#Array Attriubute
arr5 = np.array([[1,2,3], [4,5,6]])
print("Shape", arr5.shape)
print("Number of Dim\n", arr5.ndim)
print("Size of an array:", arr5.size)
