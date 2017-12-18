# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:06:12 2017

@author: Alok-PC
"""


import numpy as np

#Uncomment the under section to test the code
'''

ex2 = np.full((2,2), 9.0)  
print(ex2)   

an_array = np.array([3, 33, 333]) 
print(an_array.shape)

print(an_array[0], an_array[1], an_array[2]) 

an_array[0] =888            # ndarrays are mutable, here we change an element of the array

print(an_array)

'''

#How to create a Rank 2 numpy array:
'''

another = np.array([[11,12,13],[21,22,23]])   # Create a rank 2 array

print(another)  # print the array

print("The shape is 2 rows, 3 columns: ", another.shape)  # rows x columns                   

print("Accessing elements [0,0], [0,1], and [1,0] of the ndarray: "
      , another[0, 0], ", ",another[0, 1],", ", another[1, 0])

'''

# There are many ways to create numpy arrays 

# create a 2x2 array filled with 0
example=np.zeros((2,2))
print(example)

# create a 2x2 array filled with 9.0
ex2 = np.full((2,2), 9.0)  
print(ex2)   

# create a 2x2 matrix with the diagonal 1s and the others 0
ex3 = np.eye(2,2)
print(ex3)  

ex4 = np.ones((2,2))
print(ex4)    

# notice that the above ndarray (ex4) is actually rank 2, it is a 2x1 array
print(ex4.shape)

# which means we need to use two indexes to access an element
print()
print(ex4[0,1])

# create an array of random floats between 0 and 1
ex5 = np.random.random((2,2))
print(ex5)    









