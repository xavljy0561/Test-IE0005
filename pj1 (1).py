#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# In[2]:


stores = pd.read_csv('C:\\Users\\xavie\\OneDrive\\Desktop\\py1\\Stores.csv')


# In[3]:


stores


# In[4]:


plt.scatter(x = "Store_Area", y = "Store_Sales", data = stores)


# In[5]:


plt.scatter(x = "Daily_Customer_Count", y = "Store_Sales", data = stores)


# In[6]:


sb.pairplot(stores)


# In[9]:


area_item=pd.DataFrame(stores[['Store_Area','Items_Available']])


# In[10]:


sb.jointplot(data = stores, x = "Store_Area", y = "Items_Available", height = 12)


# In[ ]:





# In[ ]:




