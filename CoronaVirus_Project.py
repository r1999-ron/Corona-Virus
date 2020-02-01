#!/usr/bin/env python
# coding: utf-8

# The 2019-nCoV is a contagious coronavirus that hailed from Wuhan, China. This new strain of virus has striked fear in many countries as cities are quarantined and hospitals are overcrowded. This dataset will help us understand how 2019-nCoV is spread aroud the world.

# In[1]:


#Important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('2019_nCoV_20200121_20200130.csv')
data.head()


# In[3]:


data.info()


# In[4]:


unique_dates = list(data['Last Update'].unique())
unique_dates.sort()
unique_dates


# In[5]:


#Remove redundants 
excess_time = ['1/24/2020 4:00 PM', '1/25/2020 10:00 PM', '1/25/2020 12:00 AM','1/26/2020 11:00 AM', '1/27/2020 9:00', '1/28/2020 13:00']
for i in excess_time:
    unique_dates.remove(i)


# In[6]:


#Graphing the no of confirmed deaths,cases and mortaility over time
world_cases=[]
deaths=[]
mortality_rate=[]
for i in unique_dates:
    confirmed_sum = data[data['Last Update']==i].Confirmed.sum()
    death_sum = data[data['Last Update']==i].Death.sum()
    world_cases.append(confirmed_sum)
    deaths.append(death_sum)
    mortality_rate.append(death_sum/confirmed_sum)


# In[7]:


plt.figure(figsize=(10,12))
plt.plot(unique_dates,world_cases)
plt.title('Coronavirus Cases Over Time', size=30)
plt.xlabel('Time', size=30)
plt.ylabel('No of Cases',size=30)
plt.xticks(rotation=50,size=15)
plt.show()


# In[8]:


plt.figure(figsize=(10,12))
plt.plot(unique_dates,deaths,color='red')
plt.title('Coronovirus Deaths Over Time',size=30)
plt.xlabel('Time',size=30)
plt.ylabel('No of Deaths',size=30)
plt.xticks(rotation=50,size=15)
plt.plot()


# In[9]:


plt.figure(figsize=(10,12))
plt.plot(unique_dates, mortality_rate, color='orange')
plt.title('Mortality Rate Of Coronovirus Over Time', size=30)
plt.xlabel('Time', size=30)
plt.ylabel('Mortality Rate', size=30)
plt.xticks(rotation=50, size=15)
plt.plot()


# In[10]:


latest_date = '1/30/2020 21:30'
data[data['Last Update']==latest_date]


# In[11]:


#no of cases per province/city/state
unique_countries = data[data.Confirmed>0][data['Last Update']==latest_date]['Country/Region'].unique()
unique_countries.sort()
unique_countries


# In[12]:


#Count the cases for each country/territory
country_confirmed_cases=[]
for i in unique_countries:
    country_confirmed_cases.append(data[data.Confirmed>0][data['Last Update']==latest_date][data['Country/Region']==i][data['Last Update']==latest_date].Confirmed.sum())


# In[13]:


#provinces/countries having confirmed death
unique_provinces = data['Province/State'][data['Last Update']==latest_date][data.Confirmed>0].unique()
unique_provinces


# In[14]:


province_confirmed_cases=[]
for i in unique_provinces:
    province_confirmed_cases.append(data[data.Confirmed>0][data['Last Update']==latest_date][data['Province/State']==i][data['Last Update']==latest_date].Confirmed.sum())


# In[15]:


#Remove Nan Values from unique_provinces
nan_indices=[]
for i in range(len(unique_provinces)):
    if type(unique_provinces[i])==float:
        nan_indices.append(i)
unique_provinces = list(unique_provinces)
province_confirmed_cases = list(province_confirmed_cases)

for i in nan_indices:
    unique_provinces.pop(i)
    province_confirmed_cases.pop(i)


# In[16]:


# no of cases per country/region
for i in range(len(unique_countries)):
    print(f'{unique_countries[i]}: {country_confirmed_cases[i]} cases')


# In[17]:


#no of cases per province/states
for i in range(len(unique_provinces)):
    print(f'{unique_provinces[i]}: {province_confirmed_cases[i]} cases')


# In[26]:


plt.figure(figsize=(20,10))
plt.barh(unique_countries, country_confirmed_cases)
plt.title('Number of patients confirmed infected by Corona Virus, By Countries')
plt.plot()


# In[25]:


plt.figure(figsize=(20,10))
plt.title('Number of patients confirmed infected by Corona Virus, By States')
plt.barh(unique_provinces, province_confirmed_cases)
plt.plot()


# In[20]:


plt.figure(figsize=(10,10))
plt.pie(country_confirmed_cases)
plt.legend(unique_countries,loc='best')
plt.show()


# In[21]:


plt.figure(figsize=(10,10))
plt.pie(province_confirmed_cases)
plt.legend(unique_provinces,loc='best')
plt.show()


# In[ ]:




