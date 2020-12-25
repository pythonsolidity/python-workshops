#!/usr/bin/env python
# coding: utf-8

# # Numpy

# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

# In[ ]:


import numpy as np


# In[ ]:


arr = np.array([1,2])


# In[ ]:


print(arr)
print(type(arr))
print(arr.shape)
print(arr.size)


# In[ ]:


arr2 = np.array([[1,2,3],[4,5,6]])


# In[ ]:


print(arr2)
print(type(arr2))
print(arr2.shape)
print(arr2.size)


# In[ ]:


arr2[:,0:2]


# In[ ]:


arr2[0,:]


# In[ ]:


arr2


# ### Built in function

# In[ ]:


arr = np.zeros((4,3))
arr


# In[ ]:


arr = np.ones((4,4))
arr


# In[ ]:


arr = np.random.random((4,4))
arr


# In[ ]:


arr = np.full((4,4),6)
arr


# ### Reshaping an array

# In[ ]:


arr.reshape(2,2,4)


# ### Flatten an array

# In[ ]:


arr = np.random.random((2,4))
arr


# In[ ]:


arr.flatten()


# # Operators

# ### Unary Operator

# In[ ]:


arr = np.array([[1,2,3],
                [4,5,6]])
print(arr.min())  # finding min
print(arr.max())  # finding max
print(arr.sum())  # finding sum


# ### Binary operators

# In[ ]:


arr1 = np.array([1,2])
arr2 = np.array([3,4])
print(arr1 + arr2) #sum of two array elementwise
print(arr1 * arr2) #multiply of two array elementwise
print(arr1.dot(arr2)) #sum of two array elementwise


# ## Matrix Multiplication

# In[ ]:


m1 = np.array([[1,2],[3,4]])
m2 = np.array([[2,4],[4,4]])
np.matmul(m1,m2)


# ## Sorting array

# In[ ]:


arr = np.random.random((4,3))
arr


# In[ ]:


np.sort(arr, axis = 1)


# In[ ]:


np.sort(arr, axis = 0)


# In[ ]:




