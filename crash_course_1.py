print ("My name is {} and my age is {}".format("azan",21))
# another way
print ("My name is {one} and my age is {two}".format(one="azan",two=21))
# lists
mlist = []
# tuples
mtuple = ()
# Difference b/w list and tuple is that list in mmutable i.e its elenents can be changed but tuple is immuatable

# mlist[0] = 1  is valied
# mtuple[0] = 1  is In-valied

# sets

mset = {1,2,3}

# set can only contain distinct elements

#getting unique elements form a list

unique = set([1,2,2,2,2,2,3,3,3,3,3,4])
print(unique)

# string comparions
print("23" != "32") # true 

# for each

for i in [1,2,3,4,4]:
    print(i)

#List comprihension

# syntax:
# [statement for ]
    
mlist = [x**2 for x in range (10)]
print(mlist)

# Map

# map is used to execute a fuinction on each element of a list and return an address
mlist = [1,2,3]
def multiply(n):
    return n*2
print(list(map(multiply,mlist)))

# Lambda expression or anonymous function
lambda var: var*2 # here var is parameter and after : is the value return by function
# another way
t =  lambda var: var*2

print(t(2))

# filter expression
# Syntax:
# filter(filter lamda, list)

# get even numbers from a list

mlist = [x for x in range(10)]

print(list(filter(lambda x: x%2 == 0 , mlist)))



