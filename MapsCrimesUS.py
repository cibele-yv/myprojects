#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# In[2]:


df_incidents = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe!')


# In[3]:


df_incidents.head(5)


# In[4]:


df_incidents['PdDistrict'].value_counts()


# In[11]:


df_group = df_incidents.groupby(['PdDistrict']).size().reset_index(name='count')
df_group


# In[6]:


# download countries geojson file
get_ipython().system('wget --quiet https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/world_countries.json -O world_countries.json')
    
print('GeoJSON file downloaded!')


# In[7]:


#Folium is not available by default, so we need to install it

get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')


# In[42]:


world_geo = r'san-francisco.geojson' # geojson file


# In[43]:


# NY latitude and longitude values
# latitude = 40.73
# longitude = -73.93
# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42


# In[44]:


world_map = folium.Map(location=[latitude, longitude], zoom_start=12, tiles='Mapbox Bright')


# In[45]:


df_group


# In[46]:


# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
world_map.choropleth(
    geo_data=world_geo,
    data=df_group,
    columns=['PdDistrict', 'count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Default threshold scale'
)

# display map
world_map


# In[ ]:




