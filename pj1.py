#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# In[4]:


a1 = pd.read_csv('C:\\Users\\xavie\\OneDrive\\Desktop\\py1\\Stores.csv')


# In[5]:


a1


# In[6]:


plt.scatter(x = "Store_Area", y = "Store_Sales", data = a1)


# In[7]:


plt.scatter(x = "Items_Available", y = "Store_Sales", data = a1)


# In[8]:


plt.scatter(x = "Daily_Customer_Count", y = "Store_Sales", data = a1)


# In[10]:


sb.pairplot(a1)


# In[20]:


aai=pd.DataFrame(a1[['Store_Area','Items_Available']])


# In[25]:


sb.jointplot(data = a1, x = "Store_Area", y = "Items_Available", height = 12)


# In[ ]:




