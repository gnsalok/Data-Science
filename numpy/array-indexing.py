# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:53:11 2017

@author: Alok-PC
"""

import numpy as np
'''

# Rank 2 array of shape (3, 4)
an_array = np.array([[11,12,13,14], [21,22,23,24], [31,32,33,34]])
print(an_array)

a_slice = an_array[:2, 1:3]
print(a_slice)


print("Before:", an_array[0, 1])   #inspect the element at 0, 1  

a_slice[0, 0] = 1000    # a_slice[0, 0] is the same piece of data as an_array[0, 1]
print("After:", an_array[0, 1])   #changes perfoms in the main array as well
'''


### Use both integer indexing & slice indexing
#
## Create a Rank 2 array of shape (3, 4)
#an_array = np.array([[11,12,13,14], [21,22,23,24], [31,32,33,34]])
#print(an_array)
#
##Using both integer indexing & slicing generates an array of lower rank
#row_rank1 = an_array[1, :]    # Rank 1 view 
#
#print(row_rank1, row_rank1.shape)  # notice only a single []
#
## Slicing alone: generates an array of the same rank as the an_array
#row_rank2 = an_array[1:2, :]  # Rank 2 view 
#
#print(row_rank2, row_rank2.shape)   # Notice the [[ ]]



print()
col_rank1 = an_array[:, 1]
col_rank2 = an_array[:, 1:2]

print(col_rank1, col_rank1.shape)  # Rank 1
print()
print(col_rank2, col_rank2.shape)  # Rank 2