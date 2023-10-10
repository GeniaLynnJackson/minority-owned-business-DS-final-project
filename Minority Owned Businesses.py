#!/usr/bin/env python
# coding: utf-8

# # Import Packages

# In[168]:


import seaborn as sns
from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import metrics
import numpy as np
import pandas as pd


# # Import Minority Owned Businesses Data

# In[332]:


Minority_owned_business = pd.read_csv('C:/Users/baby_/OneDrive/Desktop/Final Project/Minority.csv', encoding='latin-1')


# In[333]:


Minority_owned_business.head()


# # Rename Columns

# ## Rename Columns 2,6,7 and 8

# In[271]:


Minority_owned_business.rename(columns={'% of total of businesses' : '% businesses total'}, inplace=True)


# In[272]:


Minority_owned_business.head()


# In[273]:


Minority_owned_business.rename(columns={'% Unable to maintain operations (Impact Covid-19)' : 'Covid Loss'}, inplace=True)


# In[274]:


Minority_owned_business.head()


# In[275]:


Minority_owned_business.rename(columns={'% Able to maintain operations at or below cuurent levels (Impact Covid- 19)' : 'Covid Survived'}, inplace=True)


# In[276]:


Minority_owned_business.head()


# In[277]:


Minority_owned_business.rename(columns={'% Able to maintain operations at or above levels (Impact Covid- 19)' : 'Covid Thrived'}, inplace=True)


# In[278]:


Minority_owned_business.head()


# # Drop Columns

# ## Drop Columns 3 and 4

# In[279]:


Minority_owned_business.drop(['Average employer per Business'], axis=1)


# In[280]:


Minority_owned_business.drop(['Average Payroll per businesses ($1,000)'], axis=1)


# # Import Minority- owned Businesses census 2017 Data

# In[281]:


Census_2017= pd.read_csv('C:/Users/baby_/OneDrive/Desktop/Final Project/Minority- owned businesses census 2017.csv', encoding='latin-1')


# In[282]:


Census_2017.head()


# # Rename Columns

# ## Rename Columns 2 and 3

# ### Rename Coulmn 2 Estimated Businesses(2017)

# In[283]:


Census_2017.rename(columns={'Estimated Businesses' : 'Estimated Businesses(2017)'}, inplace=True)


# In[284]:


Census_2017.head()


# ### Rename Column 3 Estimated Annual Receipts(2017)

# In[285]:


Census_2017.rename(columns={'Estimated Annual Receipts' : 'Estimated Annual Receipts(2017)'}, inplace=True)


# In[286]:


Census_2017.head()


# ## Separate Estimated Businesses(2017) Column from Census Data and Rename it

# In[287]:


Census_2017A = Census_2017['Estimated Businesses(2017)'].str.split('/', expand=True)


# In[288]:


Census_2017A.head()


# ## Rename New Column

# In[289]:


Census_2017A = Census_2017['Estimated Businesses(2017)'].str.split('/', expand=True).rename(columns = lambda x: "Estimated Businesses(2017)")


# In[290]:


Census_2017A.head()


# ## Add New Column to Minority_owned_business and rename Data

# In[291]:


Minority_owned_business2 = pd.concat([Minority_owned_business, Census_2017A], axis=1)


# In[292]:


Minority_owned_business2.head()


# ## Now Separate Estimated Annual Receipts(2017) From Census Data

# In[293]:


Census_2017.head()


# In[294]:


Census_2017B = Census_2017['Estimated Annual Receipts(2017)'].str.split('/', expand=True)


# In[295]:


Census_2017B.head()


# ## Rename New Column

# In[296]:


Census_2017B = Census_2017['Estimated Annual Receipts(2017)'].str.split('/', expand=True).rename(columns = lambda x: "Estimated Annual Receipts(2017)")


# In[297]:


Census_2017B.head()


# ## Add New Column to Minority_Owned_Businesses Data

# In[298]:


Minority_owned_business3 = pd.concat([Minority_owned_business2, Census_2017B], axis=1)


# In[299]:


Minority_owned_business3.head()


# # Import Minority- Owned Businesses Cenus 2019-2021 Data

# In[300]:


Census_2019_2021 = pd.read_csv('C:/Users/baby_/OneDrive/Desktop/Final Project/Minority Owned Businesses Cenus Data.csv', encoding='latin-1')


# In[301]:


Census_2019_2021.head()


# ## Rename Columns 2 and 3

# ## Rename Column 2 Estimated Businesses(2019-2021)

# In[302]:


Census_2019_2021.rename(columns={'Estimated Businesses' : 'Estimated Businesses(2019-2021)'}, inplace=True)


# In[303]:


Census_2019_2021.head()


# ### Rename Cloumn 3 Estimated Annual Receipts(2019-2021)

# In[304]:


Census_2019_2021.rename(columns={'Estimated Annual Receipts' : 'Estimated Annual Receipts(2019-2021)'}, inplace=True)


# In[305]:


Census_2019_2021.head()


# ## Separate Estimated Businesses(2019-2021) Column from Census Data and Rename it

# In[306]:


Census_2019_2021A = Census_2019_2021['Estimated Businesses(2019-2021)'].str.split('/', expand=True)


# In[307]:


Census_2019_2021A


# ### Rename New Column Estimated Businesses(2019-2021)

# In[308]:


Census_2019_2021A = Census_2019_2021['Estimated Businesses(2019-2021)'].str.split('/', expand=True).rename(columns = lambda x: "Estimated Businesses(2019-2021)")


# In[309]:


Census_2019_2021A.head()


# ### Add New Column to Minority_owned_business and rename Data

# In[310]:


Minority_owned_business4 = pd.concat([Minority_owned_business3, Census_2019_2021A], axis=1)


# In[311]:


Minority_owned_business4.head()


# ## Separate Estimated Annual Receipts(2019-2021) Column from Census Data and Rename it

# In[312]:


Census_2019_2021B = Census_2019_2021['Estimated Annual Receipts(2019-2021)'].str.split('/', expand=True)


# In[313]:


Census_2019_2021B.head()


# ### Rename New Coulmn

# In[314]:


Census_2019_2021B = Census_2019_2021['Estimated Annual Receipts(2019-2021)'].str.split('/', expand=True).rename(columns = lambda x: "Estimated Annual Receipts(2019-2021)")


# In[315]:


Census_2019_2021B.head()


# ### Add New Column to Minority_owned_business and rename Data

# In[329]:


Minority_owned_businesses = pd.concat([Minority_owned_business4, Census_2019_2021B], axis=1)


# In[330]:


Minority_owned_businesses.head()


# ## Drop Column 4 Average employer per Business

# In[331]:


Minority_owned_businesses.drop(['Average Payroll per businesses ($1,000)'], axis=)


# ## Drop Column 5 Average Payroll per businesses

# In[324]:


Minority_owned_businesses.drop(['Average employer per Business'], axis=1)


# ## Drop Column 6 Covid Loss

# In[320]:


Minority_owned_businesses.drop(['Covid Loss'], axis=1)


# # Import Businesses Owned by Black Women Data

# In[92]:


Black_Women_Owned= pd.read_csv('C:/Users/baby_/OneDrive/Desktop/Final Project/Businesses owned by Black Women.csv', encoding='latin-1')


# In[93]:


Black_Women_Owned.head()


# In[ ]:




