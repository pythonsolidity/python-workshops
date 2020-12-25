#!/usr/bin/env python
# coding: utf-8

# # Tensorflow 2.0

# In[ ]:


import tensorflow as tf
tf.__version__           # check version. Version 2.0 is quite different from 1.0.


# ## Eager Execution

# Previously in tensorflow, expresion were not evaluated directly. Instead, computation graph were generated and these graphs were evaluated inside a session. But now eager execution has been introduced, which means expresions are evaluated immediately and concrete values are returned. This results in speed up and a number of other advantages.

# ### Declaring eager variables

# In[ ]:


v0 = 42  #python variable
v1 = tf.Variable(42) #dimension/rank 0 tensor
v2 = tf.Variable([1,2]) #dimesntion/rank 1 tensor. It is like a python list or numpy array
v3 = tf.Variable([[1,2],[3,4]])  #dimension/rank 3 tensor. It is like a matrix (2 dimensional list or array).


# In[ ]:


v0


# In[ ]:


# numpy = value of the variable, the rest of the fields display data type and size

v1


# In[ ]:


v2


# In[ ]:


v3


# To reassign a variable, use var.assign()

# In[ ]:


# instead of assigning by using '=', tensorflow variables require the assign() method.

v1.assign(33)
v1


# ### Declaring TensorFlow constants

# In[ ]:


# constants cannot be reassigned, their values remain unchanged within a program.
# good to store information that should not change

c1 = tf.constant(42)
c1


# you can explicitly specify the datatype

# In[ ]:


c2 = tf.constant(62,dtype = tf.float64)
c2


# ### Shaping a tensor

# In[ ]:


t4 = tf.Variable([[1,2,3],[4,5,6]])
t4.shape


# or you can reshape a tensor

# In[ ]:


t5 = tf.reshape(t4,[1,6])
t5.shape


# In[ ]:


t5


# ### Rank/Dimensions of a tensor

# The rank of a tensor is the number of dimensions it has, that is, the number of indices that are required to specify any particular element of that tensor.

# In[ ]:


tf.rank(t4)


# ### Specifying an element of a tensor

# In[ ]:


t6 = t4[0,0]
t6


# ### Casting a tensor to NumPy

# In[ ]:


# now only the value is displayed and the data type and shape are hidden
t6.numpy()


# ### Finding the number of elements of a tensor

# In[ ]:


tf.size(input = t4).numpy()


# ### Finding the datatype of a tensor

# In[ ]:


t6.dtype


# ### Type casting

# In[ ]:


# by python default, the data type of c1 is int
c1


# In[ ]:


# you can change it to float
c3 = tf.cast(c1,dtype = tf.float64)
c3


# ### Declaring ragged tensors

# A ragged tensor is a tensor with one or more ragged dimensions. Ragged dimensions are dimensions that have slices that may have different lengths.

# In[ ]:


# The lists in the tensor have different lengths

ragged = tf.ragged.constant([[1],[],[1,2],[3,4,5]])
ragged


# ## Tensorflow Operations

# ### Add two tensors

# In[ ]:


v1 = tf.Variable([3,4])
v2 = tf.Variable([2,1])
v1 + v2


# In[ ]:


# operations are applied between tensor elements that are in the same position
# multiplication *, subtraction -, and divistion / are performed in the same manner

t7 = tf.Variable([1,2])
t8  = tf.Variable([2,2])
t7*t8


# In[ ]:


(t7*4).numpy()


# ### Matrix Multiplication

# In[ ]:


# if you know how matrix multiplication is performed (high school/college math)
# don't worry if you don't understand this part

c1 = tf.constant([[1,2], [3,4]])
c2 = tf.constant([[5,6], [7,8]])
tf.matmul(c1, c2)


# ### Concatinate two tensors

# In[ ]:


v1 = tf.Variable([[1,2],
                  [3,4]])
v2 = tf.Variable([[6,7],
                  [8,9]])
v3 = tf.concat(values = [v1,v2],axis = 0)
v3


# In[ ]:


v4 = tf.concat(values = [v1,v2],axis = 1)
v4


# ### Finding minimum and maximum element

# In[ ]:


v1 = tf.Variable([4,2,3,5])
tf.argmax(input = v1).numpy()


# In[ ]:


tf.argmin(input = v1).numpy()


# ## Saving and restoring tensor values using a checkpoint

# In[ ]:


# as we perform computations, the value of a variable may change 
# we can save these different values y declaring different variables
# but this is not memory efficient. imagine saving a large dataset over and over again in memory!
# checkpoints can be used to save different states of the same variable in files on your storage (rather than memory)

variable = tf.Variable([[1,2],[3,4]])
checkpoint = tf.train.Checkpoint(var = variable)
save_path = checkpoint.save('./vars')


# In[ ]:


save_path


# In[ ]:


variable.assign([[0,0],[0,0]])
variable


# In[ ]:


# you can restore an older state of the variable using a saved checkpoint

checkpoint.restore(save_path)


# In[ ]:


# the variable has been restored to its original value

variable


# In[ ]:




