#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import warnings


# In[23]:


bankData1 = pd.read_csv(r'/Applications/bankData1.csv')


# In[34]:


bankData1.head()
bankData1.tail()


# In[27]:


bankData1['expected_recovery_amount'].max()


# In[28]:


bankData1['expected_recovery_amount'].min()


# In[29]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
plt.scatter(x=bankData1['expected_recovery_amount'],y=bankData1['actual_recovery_amount'])
plt.xlabel('expected_recovery_amount')
plt.ylabel('actual_recovery_amount')
plt.show()


# In[30]:


plt.figure(figsize=(16,6))
sns.lineplot(data=bankData1)

