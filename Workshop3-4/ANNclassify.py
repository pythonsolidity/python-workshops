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


dataset = pd.read_csv('marketing.csv')
dataset


# In[ ]:


dataset.describe()


# In[ ]:


# Separate Independent variables (X) and dependent variable (y)

X = dataset.iloc[:, 0:3].values
y = dataset.iloc[:, 3].values

print(X,'\n\n', y)


# ### Missing values

# In[ ]:


# Replace missing values by the column/variable average (mean)
# Import Class --> Create Object --> Fit Object to Data --> Transform Data

from sklearn.impute import SimpleImputer                            #import the SimpleImputer class
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')     #create the imputer object

imputer.fit(X[:, 1:])                          #fit the object to the data
X[:, 1:] = imputer.transform(X[:, 1:])        #transform data

print(X)


# ### Encoding categorical variables

# In[ ]:


# Encoding independent variables
# Import Class --> Create Object --> Fit Object to Data --> Transform Data

from sklearn.compose import ColumnTransformer       # import class
from sklearn.preprocessing import OneHotEncoder     # import class

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop = 'first'), [0])], remainder='passthrough')    
#create object

X = np.array(ct.fit_transform(X))                   # fit object to data and transform data

print(X)


# In[ ]:


# Encoding dependent variable because this is a classification problem. The dependent variable is categorical.
# Import Class --> Create Object --> Fit Object to Data --> Transform Data

from sklearn.preprocessing import LabelEncoder   #import class
le = LabelEncoder()                              #create object
y = le.fit_transform(y)                          #fit and transform

print(y)


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


# # Artificial Neural Net (ANN) for Classification

# ### Training the Model

# We previously used Logistic Regression for classification. Now we use ANNs. 

# In[ ]:


# We use ANNs. 
# Can also use logistic regression, support vector machine, decision trees or random forest classification.  

# Import Class --> Create Object --> Fit Object to Data --> Predict

import tensorflow as tf               # import class
from tensorflow import keras

classifier = keras.Sequential([
      tf.keras.layers.Dense(20, activation=tf.nn.relu),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(20, activation=tf.nn.relu),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])                                                              # create object with the required layers

classifier.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])                             # compile object selecting options

classifier.fit(X_train, y_train, epochs= 50)       # fit object and decide the number of epochs


# ### Testing the Model

# In[ ]:


# make predictions on the test set
# for each row in X_test, the classifier returns probabilities of being in class 0 and class 1

y_prob = classifier.predict(X_test)
print(y_prob)


# In[ ]:


# figure out y_pred

y_pred = np.argmax(y_prob, axis = 1)
print(y_pred)


# In[ ]:


df = pd.DataFrame({'y_pred': y_pred, 'y_test': y_test})     # compare

# The following command allows you to set the number of rows of the data frame that will be displayed
# If you ever wish to change the number of rows back to 10, you would need to execute the command again
# with 100 replaced by 10

pd.set_option('display.max_rows', 10)

df


# In[ ]:


# determine model accuracy on the test set

loss, acc = classifier.evaluate(X_test, y_test)   
print('Accuracy = ', acc)


# ### Confusion Matrix

# Instead of computing the number of errors manually, you can use the <b>confusion matrix</b>. It displays correct predictions in the top-left and bottom-right cells, and errors in top-right and bottom-left cells. For example, the following confusion matrix shows 
# <img src="confusion.png" width=360 />
# 150 correct predictions and 15 errors. So 
# \begin{equation*}
# Accuracy = \dfrac{correct\ predictions}{total\ predictions}\times 100 = \dfrac{150}{165} \times 100 = 91\%
# \end{equation*}

# In[ ]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)


# ## Graphing

# In[ ]:


import seaborn as sns
sns.heatmap(cm, annot=True, center = 100)


# ### Forecasting (Optional)

# In[ ]:


# Predict if a 28 year old male with 50,000 salary would make the purchase
# What happens if you change the salary to 200,000?

Z = sc.transform([[1, 28, 50000]])       # scale data by .transform() method but NOT .fit_transform()

probability = classifier.predict(Z)

forecast = np.argmax(probability, axis = 1)
print('scaled features = ', Z, ', forecast =', forecast)


# In[ ]:




