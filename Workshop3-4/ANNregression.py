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


# # Artificial Neural Net (ANN) for Regression

# ### Training the Model

# In[ ]:


# We use ANNs. 
# Can also use linear, polynomial, support vector, decision trees or random forest regression.  

# Import Class --> Create Object --> Fit Object to Data --> Predict

import tensorflow as tf               # import class
from tensorflow import keras

regressor = keras.Sequential([
    tf.keras.layers.Dense(units = 20, input_dim=5, activation='relu'),
    tf.keras.layers.Dense(units = 20, activation='relu'),
    tf.keras.layers.Dense(units = 20, activation='relu'),
    tf.keras.layers.Dense(units = 10, activation='relu'),
    tf.keras.layers.Dense(units = 1, activation = 'linear')
])                                                         # create object with the required layers

regressor.compile(
              loss='mean_squared_error',
              optimizer=tf.keras.optimizers.RMSprop(0.01),
              batch_size=20,
              metrics=['mean_absolute_error']
)                                                          # compile object selecting options

regressor.fit(X_train, y_train, epochs= 500)               # fit object and decide the number of epochs


# ### Testing the Model

# In[ ]:


# make predictions for test data

y_pred = regressor.predict(X_test).flatten()    # predict (flatten() reshapes y_pred to a one-dimensional array)

err = abs(y_test - y_pred)
df = pd.DataFrame({'y_pred': y_pred, 'y_test': y_test, 'error': err})     # compare
df


# In[ ]:


# determine model accuracy on the test set

loss, mae = regressor.evaluate(X_test, y_test, verbose=0)
print('Mean Absolute Error =', mae)


# ### Graphing (Optional)

# In[ ]:


plt.bar(range(10), err)


# In[ ]:


plt.bar(range(10), y_test)


# ### Forecasting (Optional)

# In[ ]:


# What is the profit for 
# a California startup spending 10,000 on R&D, 50,000 on Administration and 10,000 on Marketing
# What happens if they spend 100,000 on R&D?

Z = sc.transform([[0, 0, 10000, 50000, 10000]])     # scale data using .transform() method but NOT .fit_transform()

prediction = regressor.predict(Z)
print('Scaled features = ', Z, ', Forecast = ', prediction)


# In[ ]:




