import numpy as np

arr =  np.array([1,2,3,4])

arr_view = arr.view()
arr_view[0] = 100
print("original array after view", arr)

arr_copy = arr.copy()
arr_copy[1] = 200
print("Original array after modifying it ", arr)


# arr = np.arange(1,13).reshape(3,4)
# print("original array", arr)

# spilt_arr = np.hsplit(arr, 2)
# print("Spliting an array along column", spilt_arr)

# split_arr_rows=  np.vsplit(arr,3)
# print("Split along rows", split_arr_rows)


# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])

# concat0 = np.concatenate((arr1, arr2), axis=0)
# print("Concatenate ", concat0)

# concat1 = np.concatenate((arr1, arr2), axis=1)
# print("Concatenate coulmn", concat1)

# vstacked = np.vstack((arr1, arr2))
# print("Vertical Stack", vstacked)

# hstacked = np.hstack((arr1, arr2))
# print("Horizantal Stack", hstacked)

# arr = np.arange(1,13)
# print("Original Array",arr)
# # reshape 
# arr_reshaped = arr.reshape(3,4)
# print("Reshaped Array", arr_reshaped)
# # flatten array
# print("flattened array", arr_reshaped.flatten())
# # revel 
# print("Flatten Array", arr.ravel())

# # Trnaspose array
# arra2d= np.array([[1,2,3], [4,5,6]])
# print("Original Array", arra2d)

# arr_transpose = arra2d.T
# print("Tranposen array",arr_transpose)