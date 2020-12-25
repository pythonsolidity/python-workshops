#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing

# ### Importing the libraries

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ### Reading the dataset

# In[ ]:


dataset = pd.read_csv('startups.csv')
dataset


# In[ ]:


dataset.describe()


# In[ ]:


# Separate Independent variables (X) and dependent variable (y)

X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

print(X,'\n\n', y)


# ### Missing values

# In[ ]:


# Replace missing values by the column/variable average (mean)
# Import Class --> Create Object --> Fit Object to Data --> Transform Data

from sklearn.impute import SimpleImputer                            #import the SimpleImputer class
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')     #create the imputer object

imputer.fit(X[:, 0:3])                          #fit the object to the data
X[:, 0:3] = imputer.transform(X[:, 0:3])        #transform data

print(X)


# ### Encoding categorical variables

# In[ ]:


# Encoding independent variables
# Import Class --> Create Object --> Fit Object to Data --> Transform Data

from sklearn.compose import ColumnTransformer       # import class
from sklearn.preprocessing import OneHotEncoder     # import class

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop = 'first'), [3])], remainder='passthrough')    
#create object

X = np.array(ct.fit_transform(X))                   # fit object to data and transform data

print(X)


# ### Feature scaling

# In[ ]:


# Adjusting the scales of independent variables 
# Import Class --> Create Object --> Fit Object to Data --> Transform Data

from sklearn.preprocessing import StandardScaler   # import class
sc = StandardScaler()                              # create object
X = sc.fit_transform(X)                            # fit and transform 

print(X)


# In[ ]:


df = pd.DataFrame(X)
df.describe()


# ### Splitting the dataset into the Training set and Test set

# In[ ]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[ ]:


print(X_train)


# # Regression

# ### Training the Model

# In[ ]:


# We use linear regression. 
# Can also use polynomial, support vector, decision tree or random forest regression.  

# Import Class --> Create Object --> Fit Object to Data --> Predict

from sklearn.linear_model import LinearRegression   # import class
regressor = LinearRegression()                      # create object
regressor.fit(X_train, y_train)                     # fit object


# ### Testing the Model

# In[ ]:


# make predictions for test data

y_pred = regressor.predict(X_test)    # predict

err = abs(y_pred - y_test)

df = pd.DataFrame({'y_pred': y_pred, 'y_test': y_test, 'error': err})     # compare
df


# In[ ]:


df.describe()


# In[ ]:


# mean absolute error (MAE)
print('MAE = ', df['error'].mean())


# ### Graphing (Optional)

# In[ ]:


plt.bar(range(10), err)


# In[ ]:


plt.bar(range(10), y_test)


# In[ ]:


plt.scatter(X_test[:,2], y_test, color = 'red')
#plt.plot(X_test[:,2], y_pred, color = 'blue')
plt.title('Linear Regression')
plt.xlabel('X variable')
plt.ylabel('Profit')
plt.show()


# ### Forecasting (Optional)

# In[ ]:


# What is the profit for 
# a California startup spending 10,000 on R&D, 50,000 on Administration and 10,000 on Marketing
# What happens if they spend 100,000 on R&D?

Z = sc.transform([[0, 0, 10000, 50000, 10000]])     # scale data using .transform() method but NOT .fit_transform()

prediction = regressor.predict(Z)
print(Z, prediction)


# In[ ]:




