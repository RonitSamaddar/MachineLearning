#numpy = Numerical Python, essential library used to define multidimensional array objects and 
#        contains functions for various mathematical operations on such arrays

import numpy as np

# 1) Creating numpy array from a list

#Single dimensional
lst=[1,2,3]
nplist=np.array(lst)
print(type(nplist))
print(nplist)
print(nplist.shape)#Used for getting dimensions of numpy array
print("\n")
#Multi dimensional
lst=[[1,2,3],[4,5,6]]
nplist2=np.array(lst)
print(type(nplist))
print(nplist)
print(nplist.shape)
print("\n")

# 2) Setting datatype of numpy array
nplist2=np.array(lst,dtype=complex)
print(type(nplist2))
print(nplist2)
print(nplist2.shape)
print("\n")

# 3) Reshaping a numpy array
nplist.resize((3,2))
print(type(nplist))
print(nplist)
print(nplist.shape)
print("\n")

# 4) Creating an empty numpy array (will contain random values as non-initialized)
nplist4=np.empty(shape=[2,3],dtype=float)
print(type(nplist4))
print(nplist4)
print(nplist4.shape)
print("\n")

# 5) Creating an numpy array of zeroes
nplist5=np.zeros(shape=[2,3],dtype=float)
print(type(nplist5))
print(nplist5)
print(nplist5.shape)
print("\n")
#Same way for ones
nplist5=np.ones(shape=[2,3],dtype=float)
print(type(nplist5))
print(nplist5)
print(nplist5.shape)
print("\n")

# 6) Creating a numpy array containing evenly spaced values in a range
nplist6=np.arange(0,11,2.5,dtype=float)#we want values from 0 to 10 at steps of 2.5
print(type(nplist6))
print(nplist6)
print(nplist6.shape)
print("\n")

# 7) Creating a numpy array containing evenly spaced values in a range
nplist7=np.linspace(0,10,5,dtype=float)#we want 4 values from 0 to 10
print(type(nplist7))
print(nplist7)
print(nplist7.shape)
print("\n")

# 8) Slicing a numpy array
npl=np.array([[1,2,3],[4,5,6],[7,8,9]])
nplist8=npl[:,0:2]#Take all rows(':') and columns >= 0 and < 2 i.e. 0,1
print(type(nplist8))
print(nplist8)
print(nplist8.shape)
print("\n")
nplist8=npl[0::2,:]#Take all rows at a step of 2 (i.e 0 and 2)
print(type(nplist8))
print(nplist8)
print(nplist8.shape)
print("\n")

# 9) Element wise multiplication in numpy array
a=np.array([1,2,3,4])
b=np.array([20,30,10,40])
nplist9=a*b
print(nplist9)
nplist9=np.multiply(a,b)
print(nplist9)

# 10) Broadcasting in numpy
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1],[2],[3]])
nplist10=a*b # a is of size 3*3, b is of size 3*1, broadcasting ensures a is multiplied by [b,b,b] of shape 3*3
print(nplist10)
print(nplist10.shape)
print("\n")

# 11) Flattening an array
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
nplist11=a.flatten() 
print(nplist11)
print(nplist11.shape)
print("\n")

# 12) Transposing an array
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
nplist12=a.T
print(nplist12)
print(nplist12.shape)
print("\n")

# 13) Concatenating an array
a=np.array([1,2,3])
b=np.array([4,5,6])
nplist13=np.concatenate((a,b));
print(nplist13)
print(nplist13.shape)
print("\n")
# 14) Matrix multiplication
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.T
nplist14=np.dot(a,b) 
print(nplist14)
print(nplist14.shape)
print("\n")




