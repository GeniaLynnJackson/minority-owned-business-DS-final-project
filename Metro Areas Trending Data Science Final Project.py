#!/usr/bin/env python
# coding: utf-8

# # Load Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import metrics
from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# ## Import the data

# ### Metro Areas with the highest percentage of Black owned employer businesses 2020

# In[3]:


MetroAreasTrending = pd.read_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/Metro Areas Trending.csv")


# In[4]:


MetroAreasTrending.head()


# ### Rename the data

# In[5]:


MetroAreasTrending.rename(columns = {'Number of Black Businesses': 'Number of Black Businesses for 2020'}, inplace = True)


# In[9]:


MetroAreasTrending.rename(columns = {'% Black Business': '% Black Business for 2020'}, inplace = True)


# In[10]:


MetroAreasTrending.head()


# ### Remove unnecessary data

# ### Since I don't need the % of Black Population or the Ratio of % Black Businesses to % black population, I'm removing these columns.

# In[11]:


MetroAreasTrending.drop(['% Black population'], axis=1, inplace=True)


# In[12]:


MetroAreasTrending.head()


# In[13]:


MetroAreasTrending.drop(['Ratio of % Black business to % black population'], axis=1, inplace=True)


# In[14]:


MetroAreasTrending.head()


# In[52]:


MetroAreasTrending.info()


# ## Importing the Second Data Set

# ### Metro Areas with the highest number of Black-owned employers businesses 2021

# In[16]:


MetroTrending_Areas2 = pd.read_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/Metro Trending_Areas 2.csv")


# In[17]:


MetroTrending_Areas2.head()


# ### Rename the columns

# In[18]:


MetroTrending_Areas2.rename(columns = {'Number of Black Businesses': 'Number of Black Businesses for 2021'}, inplace=True)


# In[19]:


MetroTrending_Areas2.head()


# In[22]:


MetroTrending_Areas2.rename(columns = {'% Black Businesses': '% Black Businesses for 2021'}, inplace=True)


# In[23]:


MetroTrending_Areas2.head()


# ### Removing the unnecessary Data

# In[24]:


MetroTrending_Areas2.drop(['% Black Population'], axis=1, inplace=True)


# In[25]:


MetroTrending_Areas2.head()


# In[26]:


MetroTrending_Areas2.drop(['Ratio of % Black Businesses to % Black Population'], axis=1, inplace=True)


# In[27]:


MetroTrending_Areas2.head()


# In[53]:


MetroTrending_Areas2.info()


# In[ ]:




