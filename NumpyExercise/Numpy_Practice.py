# -*- coding: utf-8 -*-

#Numpy practice

#importing numpy

import numpy as np

# Create an array of 10 zeros

tza = np.zeros(10)

# Create an array of 10 ones

tna = np.ones(10)

 # Create an array of 10 Fives
 
tfa = np.ones(10) *5

# Create an array of integers from 10 - 50

aa = np.arange(10,51)

# Create a 3x3 matrix with values ranging from 0 to 8

ab = np.arange(9).reshape(3,3)

# Create a 3x3 Identity Matrix 

ac = np.eye(3)

# Create a random number between 0 and 1

ad = np.random.rand(1)

# use numpy to generate an array of 25 random numbers from normal distribution

ae = np.random.randn(25)

# create a 10 by 10 matrix with values between 0 - 1

af = np.arange(0,100)/100
af.reshape(10,10)

# create an array of 20 linearly spacedpoints between 0 and 1

ag = np.linspace(0,1,20)

# matrix related operations

mat = np.arange(1,26).reshape(5,5)

#rows and columns selections within a matrix

#mat[2:,:]

# Sum of all values in a matrix

sumofmat = np.sum(mat)

# Get standard deviation of the values in mat

stdofmat = np.std(mat)

#get sum of all comlums in mat

sumofcolmat = mat.sum(axis = 0)