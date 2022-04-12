#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

df=pd.read_excel(r"D:\Ashu Projects\Technician Model\Delhi New\Delhi Pin Codes.xlsx")
df.head()


# In[2]:


BBox=((df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max()))
BBox


# In[3]:


m = folium.Map(location=[23.2599,77.4126], tiles='cartodbpositron', zoom_start=5)
HeatMap(data=df[['latitude', 'longitude']], radius=30).add_to(m)


# In[4]:


locations = list(zip(df.latitude, df.longitude))
icons = [folium.Icon(icon="car", prefix="fa") for _ in range(len(locations))]

cluster = MarkerCluster(locations=locations, icons=icons)
m.add_child(cluster)
m


# In[5]:


m.save(r"D:\Ashu Projects\Technician Model\Delhi New\Delhi Tx Heat Map.html")


# In[ ]:




