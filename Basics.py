# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:21:56 2017

@author: jonathan
"""

import numpy as np


''' Creating arrays '''
a = np.array([1,2,3]) # Create a rank 1 array
print(a)
print(a.shape) # Prints (3,)
a[0] = 5   # Change an element of the array
print(a)   # Prints "[5,2,3]"

# Create 2d array
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)
print(b[0,0])

# Array of all zeros
a=np.zeros((2,2))
print(a)

# Array of all ones
b = np.ones((1,2))
print(b)

# Constant array
c = np.full((2,2),7)
print(c)

# Create identity matrix
d = np.eye(2)
print(d)

# Create random array
e = np.random.random((2,2))
print(e)

'''Datatypes
Every numpy array is a grid of elements of the same type. 
Numpy provides a large set of numeric datatypes that you can 
use to construct arrays. Numpy tries to guess a datatype when 
you create an array, but functions that construct arrays usually 
also include an optional argument to explicitly specify the datatype.
 Here is an example:'''

x = np.array([1, 2])  # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])  # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.int64)  # Force a particular datatype
print(x.dtype)                        # Prints "int64"
