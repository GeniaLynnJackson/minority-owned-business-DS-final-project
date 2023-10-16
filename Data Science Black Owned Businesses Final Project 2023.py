#!/usr/bin/env python
# coding: utf-8

# # Load Libraries

# In[92]:


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

# In[2]:


MetroAreasTrending = pd.read_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/Metro Areas Trending.csv")


# In[3]:


MetroAreasTrending.head()


# ### Rename the data

# In[4]:


MetroAreasTrending.rename(columns = {'Number of Black Businesses': 'Number of Black Businesses for 2020'}, inplace = True)


# In[5]:


MetroAreasTrending.rename(columns = {'% Black Business': '% Black Business for 2020'}, inplace = True)


# In[6]:


MetroAreasTrending.rename(columns = {'% Black population': '% Black population for 2020'}, inplace = True)


# In[7]:


MetroAreasTrending.rename(columns = {'Ratio of % Black business to % black population': 'Ratio of % Black business to % black population for 2020'}, inplace = True)


# In[8]:


MetroAreasTrending.head()


# In[9]:


MetroAreasTrending.tail()


# In[10]:


MetroAreasTrending.to_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/MetroAreasTrending1.csv")


# ### Sorting by column number of black businesses vs. % of black businesses for 2020

# In[11]:


M1Sort = MetroAreasTrending.sort_values(by =['Number of Black Businesses for 2020'], ascending = False)


# In[12]:


MetroAreasTrending.head(3)


# In[13]:


MetroAreasTrending.tail(3)


# In[14]:


M1aSort = MetroAreasTrending.sort_values(by =['% Black Business for 2020'],ascending = False)


# In[15]:


MetroAreasTrending.head(3)


# In[16]:


MetroAreasTrending.tail(3)


# ## Sorting by column number of % Black population for 2020 vs. Ratio of % Black business to % black population for 2020

# In[17]:


MetroAreasTrending.to_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/MetroAreasTrending1a.csv")


# In[18]:


M1bSort = MetroAreasTrending.sort_values(by =['% Black population for 2020'],ascending = False)


# In[19]:


M1bSort.head(3)


# In[20]:


M1bSort.tail(3)


# In[21]:


M1cSort = MetroAreasTrending.sort_values(by =['Ratio of % Black business to % black population for 2020'], ascending = False)


# In[22]:


M1cSort.head(3)


# In[23]:


M1cSort.tail(3)


# ### What data types are within the data set?

# In[24]:


MetroAreasTrending.info()


# ## Importing the Second Data Set

# ### Metro Areas with the highest number of Black-owned employers businesses 2021

# In[25]:


MetroTrending_Areas2 = pd.read_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/Metro Trending_Areas 2.csv")


# In[26]:


MetroTrending_Areas2.head()


# ### Rename the data

# In[27]:


MetroTrending_Areas2.rename(columns = {'Number of Black Businesses': 'Number of Black Businesses for 2021'}, inplace=True)


# In[28]:


MetroTrending_Areas2.rename(columns = {'% Black Businesses': '% Black Businesses for 2021'}, inplace=True)


# In[29]:


MetroTrending_Areas2.rename(columns = {'% Black Population': '% Black Population for 2021'}, inplace=True)


# In[30]:


MetroTrending_Areas2.rename(columns = {'Ratio of % Black Businesses to % Black Population': 'Ratio of % Black Businesses to % Black Population for 2021'}, inplace=True)


# In[31]:


MetroTrending_Areas2.head()


# In[32]:


MetroTrending_Areas2.tail(3)


# ## Sorting by columns of Number of Black Businesses vs. % Black Businesses for 2021

# In[33]:


M2Sort = MetroTrending_Areas2.sort_values(by =['Number of Black Businesses for 2021'], ascending = False)


# In[34]:


MetroTrending_Areas2.head(3)


# In[35]:


MetroTrending_Areas2.tail(3)


# ## Sorting by columns of % Black Population for vs Ratio of % Black Businesses to % Black Population for 2021

# In[36]:


M2aSort = MetroTrending_Areas2.sort_values(by =['% Black Businesses for 2021'], ascending = False)


# In[37]:


MetroTrending_Areas2.head(3)


# In[38]:


MetroTrending_Areas2.tail(3)


# In[39]:


M2bSort = MetroTrending_Areas2.sort_values(by =['% Black Population for 2021'], ascending = False)


# In[40]:


MetroTrending_Areas2.head(3)


# In[41]:


MetroTrending_Areas2.tail(3)


# In[42]:


M2cSort = MetroTrending_Areas2.sort_values(by =['Ratio of % Black Businesses to % Black Population for 2021'], ascending = False)


# In[43]:


MetroTrending_Areas2.head(3)


# In[44]:


MetroTrending_Areas2.tail(3)


# In[45]:


MetroTrending_Areas2.to_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/MetroTrending_Areas2b.csv")


# ### What data types are within the data set?

# In[46]:


MetroTrending_Areas2.info()


# ## Importing 3rd Data Set

# ### Top Metro Areas with the highest percentage of businesses owned by black women 2021

# In[47]:


MetroTrending_Areas3 = pd.read_csv(r"C:\Users\genia\OneDrive\WozU-LAPTOP-INI63IK7\Final Project for Data Science\Metro Trending_Areas 3R.csv")


# In[48]:


MetroTrending_Areas3.head()


# ### Rename the data

# In[49]:


MetroTrending_Areas3.rename(columns = {'Number of Black Businesses': 'Number of Black Businesses for 2021'}, inplace=True)


# In[50]:


MetroTrending_Areas3.rename(columns = {'% Black Businesses': '% Black Businesses for 2021'}, inplace=True)


# In[51]:


MetroTrending_Areas3.rename(columns = {'% Black Population': '% Black Population for 2021'}, inplace=True)


# In[52]:


MetroTrending_Areas3.rename(columns = {'Ratio of % Black Businesses to % Black population ': 'Ratio of % Black Businesses to % Black population for 2021'}, inplace=True)


# In[53]:


MetroTrending_Areas3.columns


# In[54]:


MetroTrending_Areas3.head()


# In[55]:


MetroTrending_Areas3.tail()


# ## Sorting by columns of Number of Black Businesses vs. % Black Businesses for 2021

# In[56]:


M3Sort = MetroTrending_Areas3.sort_values(by =['Number of Black Businesses for 2021'], ascending = False)


# In[57]:


M3Sort.head(3)


# In[58]:


M3Sort.tail(3)


# In[59]:


M3aSort = MetroTrending_Areas3.sort_values(by =['% Black Population for 2021'], ascending = False)


# In[60]:


M3aSort.head(3)


# In[61]:


M3aSort.tail(3)


# ## Sorting by columns of Number of %Black Population vs. Ratio of % Black Businesses to % Black population 2021

# In[62]:


M3bSort = MetroTrending_Areas3.sort_values(by =['% Black Population for 2021'], ascending = False)


# In[63]:


M3bSort.head(3)


# In[64]:


M3bSort.tail(3)


# In[65]:


M3cSort = MetroTrending_Areas3.sort_values(by =['Ratio of % Black Businesses to % Black population for 2021'], ascending = False)


# In[66]:


M3cSort.head(3)


# In[67]:


M3cSort.tail(3)


# ### What data types are within the data set?

# In[68]:


MetroTrending_Areas3.info()


# ## Import 4th Data set

# ### Business characteristics by gender and race 2020

# In[69]:


MetroTrending_Areas4 = pd.read_excel(r"C:\Users\genia\OneDrive\WozU-LAPTOP-INI63IK7\Final Project for Data Science\MetroTrending_Areas4.xlsx")


# In[70]:


MetroTrending_Areas4.head()


# In[71]:


MetroTrending_Areas4.info()


# ## Import 5th Data set

# ### Top Metro areas with the highest percentage of businesses owned by Black women 2020

# In[72]:


MetroTrending_Areas5 = pd.read_csv("C:/Users/genia/OneDrive/WozU-LAPTOP-INI63IK7/Final Project for Data Science/MetroTrending_Areas5.csv")


# In[73]:


MetroTrending_Areas5.head()


# In[74]:


MetroTrending_Areas5.tail()


# ## Sort Columns Number of businesses vs. % of all women owned businesses

# In[75]:


M5Sort = MetroTrending_Areas5.sort_values(by =['Number of businesses'], ascending = False)


# In[76]:


M5Sort.head(3)


# In[77]:


M5Sort.tail(3)


# In[78]:


M5aSort = MetroTrending_Areas5.sort_values(by =['% of all women owned businesses'], ascending = False)


# In[79]:


MetroTrending_Areas5.head(3)


# In[80]:


MetroTrending_Areas5.tail(3)


# In[81]:


MetroTrending_Areas5.info()


# ## Histograms for the Top 3 and Bottom 3 Ratios

# In[82]:


MetroAreasTrending.hist()


# In[83]:


MetroTrending_Areas2.hist()


# In[84]:


MetroTrending_Areas3.hist()


# #### The "unnamed" graphs need to be removed. 

# In[85]:


MetroTrending_Areas4.hist()


# #### There's only one "unnamed" graph that needs to be removed. 

# In[86]:


MetroTrending_Areas5.hist()


# ## Single Histogram with Seaborn

# In[87]:


sns.pairplot(MetroAreasTrending)


# In[88]:


sns.pairplot(MetroTrending_Areas2)


# In[89]:


sns.pairplot(MetroTrending_Areas3)


# In[90]:


sns.pairplot(MetroTrending_Areas4)


# In[91]:


sns.pairplot(MetroTrending_Areas5)


# In[ ]:





# In[ ]:





# In[ ]:




