#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


# In[15]:


df = pd.read_csv("Historical_data_Population.csv")


# In[16]:


df


# In[17]:


df.info()


# In[18]:


df.describe()


# In[19]:


plt.figure(figsize=(12,6))
plt.title("Population over the year")
sns.barplot(x=df['Year'], y=df['Population']);


# In[20]:


df.plot(x="Year", y=["Population", "World Population"], kind="bar",figsize=(12, 6),title = "compare with World population")


# In[21]:


plt.figure(figsize=(12,6))
plt.title("Population over the year")
sns.lineplot(x=df['Year'], y=df["Country's Share of World Pop"]);


# In[22]:


plt.figure(figsize=(12,6))
plt.title("Density over the year")
sns.barplot(x=df['Year'], y=df['Density (P/Km²)']);


# In[23]:


plt.figure(figsize=(12,6))

sns.barplot(x=df['Year'], y=df['Yearly Change']);


# In[24]:


plt.figure(figsize=(12,6))

sns.lineplot(x=df['Year'], y=df['Yearly % Change']);


# In[25]:


plt.figure(figsize=(12,7))

sns.lineplot(x=df['Year'], y=df['Urban Pop %']);


# In[ ]:




