import numpy as np

# first numpy array
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print("Shape:", arr.shape)
print("Number of DImension:", arr.ndim)


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1+arr2)
print(arr1*arr2)