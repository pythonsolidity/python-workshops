#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# Matplotlib is an amazing visualization library in Python for 2D plots of arrays.

# In[ ]:


import matplotlib.pyplot as plt


# ### Plotting an array

# In[ ]:


x = [10,20,30]
y = [3,2,1]
plt.plot(x,y)


# ### Bar Plot

# In[ ]:


plt.bar(x,y)


# ### Scatter

# In[ ]:


plt.scatter(x,y)


# # Working with Image

# In[ ]:


import matplotlib.image as im


# In[ ]:


img = im.imread('images/python.png')
plt.imshow(img)


# In[ ]:


img.shape


# In[ ]:


img


# In[ ]:


img[0][0]


# In[ ]:


img[0][0][0]


# In[ ]:




