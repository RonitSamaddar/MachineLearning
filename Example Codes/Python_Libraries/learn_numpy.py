#numpy = Numerical Python, essential library used to define multidimensional array objects and 
#        contains functions for various mathematical operations on such arrays

import numpy as np

#Creating numpy array from a list

#Single dimensional
lst=[1,2,3]
nplist=np.array(lst)
print(type(nplist))
print(nplist)
print(nplist.shape)#Used for getting dimensions of numpy array
print("\n")
lst2=[[1,2,3],[4,5,6],[7,8,9]]
nplist2=np.array(lst2)
print(type(nplist2))
print(nplist2)
print(nplist2.shape)
