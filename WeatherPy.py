
# coding: utf-8

# In[1]:


# Dependencies
import csv
import requests as req
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
import seaborn
from citipy import citipy
import time
import random


# In[81]:


# Save config information.
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
endpoint = "http://api.openweathermap.org/data/2.5/weather"
units = "Imperial"

# Build partial query URL


# In[3]:


#Creates 2 lists of latitudes and longitutdes randomly
#Zips into a single dictionary

lats = []
lngs = []
for x in range(500):
    lats.append(random.randrange(-90,90))
    lngs.append(random.randrange(-180,180))
locs = dict(zip(lats,lngs))
#print(len(lats), len(lngs))
type(locs)


# In[82]:


#Uses Citipy to identify the nearest city with country code

locs_conv = []
weatherdata_df = pd.DataFrame(columns = ['City','Temp','Humidity','Clouds','Wind_Speed'])
response_data = []

for key,value in locs.items():
    city = citipy.nearest_city(key,value)
    locs_conv.append(city)

#locs_conv
city_counter = 0
print('Beginning Data Retrieval')
print('-----------------------------')
for location in locs_conv:
    print('Processing record '+str(city_counter)+' of '+ str(len(locs_conv))+"|"+location.city_name)
    city_counter +=1
    
    try:
        params = {
            'appid': api_key,
            'units': units,
            'q': location.city_name+","+location.country_code
        }
                     
        #print('Getting Data for #'+str(city_counter))
        
        response = req.get(endpoint, params=params).json()
        response_data.append(response)
        target_url = "http://api.openweathermap.org/data/2.5/weather?units=%s&APPID=%s&q=%s" % (params['units'],api_key,location.city_name.strip())
        
        
    except:
        continue
    
    print(target_url)
    time.sleep(1)

    
#creates a dataframe to store the responses and then save it to a csv    
response_df = pd.DataFrame(response_data)
response_df.to_csv('saved_data.csv')  



print('Data Retrieval Complete')        


# In[5]:


response_df = response_df.dropna(thresh = 3)
response_df


# In[91]:


#creates a new list that removes the errors from the response_data list
clean_rd = [s for s in response_data if s['cod']!='404' ]

#builds the lists of data using the clean_rd 
temp_data = [response['main']['temp'] for response in clean_rd]
loc_data = [response['name'] for response in clean_rd]
humid_data = [response['main']['humidity'] for response in clean_rd]
cloud_data = [response['clouds']['all'] for response in clean_rd]
wind_data = [response['wind']['speed'] for response in clean_rd]
country_data = [response['sys']['country'] for response in clean_rd]
date_data = [response['dt'] for response in clean_rd]
lat_data = [response['coord']['lat'] for response in clean_rd]
lon_data = [response['coord']['lon'] for response in clean_rd]
max_temp_data = [response['main']['temp_max'] for response in clean_rd]
#print(loc_data)
#print(clean_rd[0])

#fills the selected data into the weatherdata_df dataframe
weatherdata_df['Wind_Speed']=wind_data
weatherdata_df['Clouds']=cloud_data
weatherdata_df['Humidity']=humid_data
weatherdata_df['Temp']=temp_data
weatherdata_df['City']=loc_data
weatherdata_df['Country'] = country_data
weatherdata_df['Date'] = date_data
weatherdata_df['Lat'] = lat_data
weatherdata_df['Lng'] = lon_data
weatherdata_df['Max Temp'] = max_temp_data

#reorders the dataframe to match the example
weatherdata_df = weatherdata_df[['City','Clouds','Country','Date','Humidity','Lat','Lng','Max Temp','Wind_Speed']]
weatherdata_df.head()


# In[64]:


clean_df = pd.DataFrame(clean_rd)
clean_df.head()


# In[107]:


#creates dataframes for each plot for the sake of clean data management
temps_df = pd.DataFrame(columns = ['Temps','Lats'])
humid_df = pd.DataFrame(columns = ['Humidity','Lats'])
cloud_df = pd.DataFrame(columns = ['Cloudiness','Lats'])
wind_df = pd.DataFrame(columns = ['Wind_Speed','Lats'])

lat_data = [response['coord']['lat'] for response in clean_rd]

#fills in the latitude data values
wind_df['Lats'] = lat_data
cloud_df['Lats'] = lat_data
humid_df['Lats'] = lat_data
temps_df['Lats'] = lat_data

#fills in the requested value for each 
wind_df['Wind_Speed'] = weatherdata_df['Wind_Speed']
cloud_df['Cloudiness'] = weatherdata_df['Clouds']
humid_df['Humidity'] = weatherdata_df['Humidity']
temps_df['Temps'] = weatherdata_df['Max Temp']


# In[114]:


#creates and styles the temperature vs latitude plot

temp_plot = plt.scatter(temps_df['Lats'],temps_df['Temps'])
plt.title('City Latitude vs Max Temperature (12/9/17)')
plt.style.use('seaborn-dark')
plt.ylabel('Max Temperature (F)')
plt.xlabel('Latitude')
plt.grid()
plt.savefig('Lat_Temp.png')
plt.show()


# In[115]:


#creates and styles the humidity vs latitude plot

humid_plot = plt.scatter(humid_df['Lats'],humid_df['Humidity'])
plt.title('City Latitude vs Humidity (12/9/17)')
plt.style.use('seaborn-dark')
plt.xlim(-80,100)
plt.ylim(-20,120)
plt.ylabel('Humidity (%)')
plt.xlabel('Latitude')
plt.grid()
plt.savefig('Lat_Humid.png')
plt.show()


# In[117]:


#creates and styles the cloudiness vs latitude plot

cloud_plot = plt.scatter(cloud_df['Lats'],cloud_df['Cloudiness'])
plt.title('City Latitude vs Cloudiness (12/9/17)')
plt.style.use('seaborn-dark')
plt.xlim(-80,100)
plt.ylim(-20,120)
plt.ylabel('Cloudiness (%)')
plt.xlabel('Latitude')
plt.grid()
plt.savefig('Lat_Cloud.png')
plt.show()


# In[118]:


#creates and styles the wind speed vs latitude plot

wind_plot = plt.scatter(wind_df['Lats'],wind_df['Wind_Speed'])
plt.title('City Latitude vs Wind Speed (12/9/17)')
plt.style.use('seaborn-dark')
plt.xlim(-80,100)
plt.ylim(-5,40)
plt.ylabel('Wind Speed (mph)')
plt.xlabel('Latitude')
plt.grid()
plt.savefig('Lat_Wind.png')
plt.show()

