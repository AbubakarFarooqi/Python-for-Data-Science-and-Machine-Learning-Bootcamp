import numpy as np

# cretaing numpy array

mlist = [1,2,3]

npArray = np.array(mlist) # it will cast the list into numpy array

print(npArray)

#creating two d array or matrix using nested list

mlist = [[1,2,3],[4,5,6],[7,8,9]]

npArray = np.array(mlist)
print(npArray)

# np also provide a easy way to create arrays some are as follows

# arange method is used to create array

# npArray = np.arange(start,stop,step)
# it will generate a 1-d array
# it generte a list in the interval [start,stop) and step indicate the increase in value 
npArray = np.arange(0,10,2)
print (npArray)

# creating arrays of zeros
# syntax for creting 1d array
# np.zeros(1d dimension i.e number of col)

npArray = np.zeros(4)
print(npArray)

# syntax for creating 2d array

# npArray =  np.zeros((row,col))

npArray = np.zeros((3,5))
print(npArray)

# np.ones do the same

# creating matrix with evenly spaced elements we use linspace function of np
# npArray = np.linspace(start,end,number of elements)

npArray = np.linspace(0,10,20) # it will create 20 evenly spaces elelmets between one and 10 
print(npArray)

# creating identity matrix
# npArray = np.eye(order) 

npArray = np.eye(5) # create an identity matrix of order 5
print(npArray)

# generaating random numbers

# np.random.rand(n)
# it will generate n random nuumber in 1d format uniformally distributed b/w 0 and 1

npArray = np.random.rand(10)

# np.random.rand(n,m)
# it will generate random nuumber in 2d format in the matrix of n X m uniformally distributed b/w 0 and 1

npArray = np.random.rand(2,3)

# Generating normal distribution or gaussian distributiuon 

# np.random.randn(n)
# np.random.randn(nxm)

# generating random integers

# np.random.randint(low,high,n)
# it will generate n integers in the interval [low,high)

npArray = np.random.randint(2,10,4)
print(npArray)


#Reshaping an Array

# we can reshape an array i.e we can change its dimensions

# array.reshape(row,col)

# one thing to consider that the number of elements in array must be equla to product(row, col)


npArray = np.arange(0,12)
print(npArray)
npArray = npArray.reshape(4,3)
print(npArray)


# getting maximum and  minimum number from a array

# arr.min()
# arr.max()

print(npArray.max())

# getting index of maximum and  minimum number from a array

# arr.argmax()
# arr.argmin()

print(npArray.argmax())

# Getting shape or dimension of array

# arr.shape
# it will return a tuple

print(npArray.shape)


