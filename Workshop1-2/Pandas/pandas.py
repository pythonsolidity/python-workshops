#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. Pandas DataFrame is two-dimensional heterogeneous tabular data structure with labeled axes (rows and columns). Pandas DataFrame consists of three principal components, the data, rows, and columns.

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


data = [10,100,1000]
df = pd.DataFrame(data)
df


# In[ ]:


arr = np.array([['col1', 'col2', 'col3'], [2.3, 1.1, 2.4], [0, 0.88, 13.7]])

df2 = pd.DataFrame(arr)
df2


# In[ ]:


df2 = pd.DataFrame(arr[1:,], columns = arr[0,])
df2


# In[ ]:


df.shape


# ### Creating DataFrame from dictionary

# In[ ]:


data = {'Name':["Alice","Bob","Chris"],
       'Age':[21,49,43]}
df = pd.DataFrame(data)
df


# ### Reading a CSV file

# In[ ]:


df = pd.read_csv('Pandas Datasets/nba.csv')


# In[ ]:


df


# In[ ]:


df = pd.read_csv('Pandas Datasets/nba.csv', index_col = "Name")


# In[ ]:


df


# ### Missing values

# In[ ]:


df.isna()


# In[ ]:


df.dropna()


# In[ ]:


df


# In[ ]:


df.fillna(0)


# In[ ]:


df.iloc[0:10, 0:4]


# In[ ]:


df.iloc[[0, 2, 4, 6, 8], [3, 4, 5]]


# In[ ]:




