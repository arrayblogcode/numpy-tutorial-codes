import numpy as np

arr = np.array([10,20,30,40,50])
print("Array",arr)

print("First Element:", arr[0])
print("third elemnt:", arr[2])

# negative indexing
print("Last element:", arr[-1])

# slicing array  arr[start:stop:step]
print("Element from 1 to 3", arr[1:4])
print("every second element", arr[::2])

# multidimensonal array
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D array\n", arr2d)

#elemt row 1 and col2 
print("Elemet at row1 and col2", arr2d[1,2])
# first row of 2d array
print("First Row", arr2d[0])
# first column
print("First column", arr2d[:,0])


# fancy indexing
arr1 = np.array([1,2,3,4,5,6])
indices = [0,3,4]
print("Slected elemets:", arr1[indices])

#boolean indexing  arr = np.array([10,20,30,40,50])
bool_idx = arr>20
print("Boolean array:", bool_idx)
print("Elements greater than 20", arr[bool_idx])




