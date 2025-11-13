import numpy as np
import time



arr = np.array([1,2,3])
scalar = 10

print("Array+scalar", arr+scalar)


# universal function n
arr1 = np.array([1,4,9,16])
print("Square root", np.sqrt(arr1))

print("Expoen", np.exp(arr1))

# arr1 = np.array([10,20,30,40])
# arr2 = np.array([1,2,3,4])

# print("Addition:", arr1+arr2)
# print("Sub:", arr1-arr2)
# print("div:", arr1/arr2)
# print("Mult:", arr1*arr2)

# list1 =[1,2,3,4,5]
# list2 = [5,4,3,2,1]

# start = time.time()
# result = [x + y for x, y in zip(list1, list2)]
# end = time.time()
# print("Python List time:", end-start)

# arr1 = np.array(list1)
# arr2 = np.array(list2)
# start1 = time.time()
# result = arr1+arr2
# end =  time.time()

# print("Numpy arraytime", end-start)