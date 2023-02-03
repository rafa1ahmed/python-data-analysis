#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the packages to use in this project

import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Downloads\1. Weather Data.csv')


# In[2]:


df


# In[3]:


df.head()


# In[5]:


df.shape


# In[6]:


df.index


# In[7]:


df.columns


# In[8]:


df.dtypes


# In[14]:


df['Weather'].unique()


# In[15]:


df.nunique()


# In[16]:


df.count()


# In[ ]:


## shows unique values with their count


# In[19]:


df['Weather'].value_counts()


# In[20]:


df.info()


# In[21]:


#find all unique wind speed data
df.head()


# In[22]:


df.nunique()


# In[23]:


df['Wind Speed_km/h'].nunique()


# In[24]:


df['Wind Speed_km/h'].value_counts()


# In[ ]:


# Find number of times when the "weather is exactly clear"



# In[26]:


df['Weather'].value_counts()


# In[27]:


df[df.Weather=='Clear']


# In[29]:


df.groupby('Weather').get_group('Clear')


# In[ ]:


# Find the number of times when the 'wind speed was exactlykm/hr' 


# In[30]:


df['Wind Speed_km/h']==4


# In[32]:


df[df['Wind Speed_km/h']==4]


# In[ ]:


#find all the null values in the data


# In[34]:


df.isnull()


# In[35]:


df.isnull().sum()


# In[36]:


df.notnull().sum()


# In[ ]:


#Rename the column whether to weather conditons


# In[39]:


df.rename(columns={'Weather':'Weather condition'})


# In[40]:


df.head()


# In[45]:


df.rename(columns={'Weather':'Weather condition'},inplace=True)


# In[46]:


df.head()


# In[ ]:


#what is the visibility mean


# In[47]:


df.Visibility_km.mean()


# In[ ]:


#what is the std deviation pf 'pressure' in this data

A standard deviation (or σ) is a measure of how dispersed the data is in relation to 
the mean. Low standard deviation means data are clustered around the mean, and high standard deviation indicates data are more spread out.


# In[48]:


df.Press_kPa.std()


# In[ ]:


#what is the variance of relative humidity in this data


# In[50]:


df['Rel Hum_%'].var()


# In[ ]:


#find all instances when snow was recorded


# In[53]:


df['Weather condition'].value_counts()


# In[55]:


df[df['Weather condition']=='Snow'] #filtering


# In[58]:


df[df['Weather condition'].str.contains('Snow')]


# In[59]:


df[df['Weather condition'].str.contains('Snow')].head(50)


# In[60]:


df[df['Weather condition'].str.contains('Snow')].tail(50)


# In[ ]:


#find all instances when 'wind speed is above 24' and visibility is 25'


# In[61]:


df.head(2)


# In[64]:


df[(df['Wind Speed_km/h']>24)&(df['Visibility_km']==25)]


# In[ ]:


#what is the mean value of each column against each weather conditions


# In[66]:


df.groupby('Weather condition').mean()


# In[ ]:





# In[ ]:


# what is the minimum and maximum valus of each column against each weather conditions


# In[67]:


df.groupby('Weather condition').min()


# In[68]:


df.groupby('Weather condition').max()


# In[ ]:


#show all records where weather condition is fog


# In[69]:


df[df['Weather condition']=='Fog']


# In[ ]:


#find all instances where 'weather condition is clear ' or visibility is 'above 40'


# In[71]:


df[(df['Weather condition']=='clear')|(df['Visibility_km']>40)]


# In[72]:


df[(df['Weather condition']=='clear')|(df['Visibility_km']>40)].head(50)


# In[76]:


df[(df['Weather condition']=='clear')&(df['Rel Hum_%']>50)|(df['Visibility_km']>40)]


# In[ ]:




