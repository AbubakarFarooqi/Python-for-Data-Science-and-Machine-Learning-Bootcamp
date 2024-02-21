import numpy as np
# slicing an array

arr = np.arange(10)

slicedArray = arr[5:]

print(slicedArray)

# it is worth to remember that sliced array is just a view of original array it is not deep copy of that elements if we chnage any element from sliced array it will also reflect in original array e.g

slicedArray[:] = 99 # setting all elements to 99
print(slicedArray)
print(arr)

# if want to make deep copy sliced array we can use copy mehtod

copy_slicedArray = slicedArray.copy()

copy_slicedArray[:] = 1
print(slicedArray)
print(copy_slicedArray)
print(arr)

# conditional slicing of array

cond_sliced_array = arr[arr >= 4] # get those elements which are gretaer than 4

print(cond_sliced_array)