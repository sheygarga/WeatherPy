

```python
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
```


```python
# Save config information.
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
endpoint = "http://api.openweathermap.org/data/2.5/weather"
units = "Imperial"

# Build partial query URL
```


```python
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
```




    dict




```python
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

```

    Beginning Data Retrieval
    -----------------------------
    Processing record 0 of 163|jhikargachha
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=jhikargachha
    Processing record 1 of 163|torbay
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=torbay
    Processing record 2 of 163|carnarvon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=carnarvon
    Processing record 3 of 163|wala
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=wala
    Processing record 4 of 163|verkhnevilyuysk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=verkhnevilyuysk
    Processing record 5 of 163|aragarcas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=aragarcas
    Processing record 6 of 163|porangatu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=porangatu
    Processing record 7 of 163|hermanus
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hermanus
    Processing record 8 of 163|vaini
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=vaini
    Processing record 9 of 163|hilo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hilo
    Processing record 10 of 163|khatanga
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=khatanga
    Processing record 11 of 163|orbetello
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=orbetello
    Processing record 12 of 163|rikitea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea
    Processing record 13 of 163|sabang
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=sabang
    Processing record 14 of 163|nuuk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=nuuk
    Processing record 15 of 163|tostamaa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=tostamaa
    Processing record 16 of 163|tiksi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=tiksi
    Processing record 17 of 163|nizhneyansk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=nizhneyansk
    Processing record 18 of 163|pospelikha
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=pospelikha
    Processing record 19 of 163|hobart
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hobart
    Processing record 20 of 163|kapaa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=kapaa
    Processing record 21 of 163|bluff
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bluff
    Processing record 22 of 163|broome
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=broome
    Processing record 23 of 163|progreso
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=progreso
    Processing record 24 of 163|galyugayevskaya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=galyugayevskaya
    Processing record 25 of 163|lasa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=lasa
    Processing record 26 of 163|burnie
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=burnie
    Processing record 27 of 163|carnarvon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=carnarvon
    Processing record 28 of 163|casper
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=casper
    Processing record 29 of 163|punta arenas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=punta arenas
    Processing record 30 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 31 of 163|mehamn
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=mehamn
    Processing record 32 of 163|turmalina
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=turmalina
    Processing record 33 of 163|severo-kurilsk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=severo-kurilsk
    Processing record 34 of 163|taolanaro
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=taolanaro
    Processing record 35 of 163|qaanaaq
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=qaanaaq
    Processing record 36 of 163|kapaa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=kapaa
    Processing record 37 of 163|hilo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hilo
    Processing record 38 of 163|takoradi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=takoradi
    Processing record 39 of 163|chavakkad
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=chavakkad
    Processing record 40 of 163|bambous virieux
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bambous virieux
    Processing record 41 of 163|lebu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=lebu
    Processing record 42 of 163|padang
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=padang
    Processing record 43 of 163|mataura
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=mataura
    Processing record 44 of 163|bethel
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bethel
    Processing record 45 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 46 of 163|bluff
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bluff
    Processing record 47 of 163|port alfred
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=port alfred
    Processing record 48 of 163|souillac
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=souillac
    Processing record 49 of 163|butaritari
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=butaritari
    Processing record 50 of 163|ibra
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ibra
    Processing record 51 of 163|saldanha
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha
    Processing record 52 of 163|hithadhoo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo
    Processing record 53 of 163|lambarene
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=lambarene
    Processing record 54 of 163|punta arenas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=punta arenas
    Processing record 55 of 163|carnarvon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=carnarvon
    Processing record 56 of 163|punta arenas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=punta arenas
    Processing record 57 of 163|castro
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=castro
    Processing record 58 of 163|manoel urbano
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=manoel urbano
    Processing record 59 of 163|walvis bay
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=walvis bay
    Processing record 60 of 163|yerofey pavlovich
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=yerofey pavlovich
    Processing record 61 of 163|avarua
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=avarua
    Processing record 62 of 163|victoria
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria
    Processing record 63 of 163|madarounfa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=madarounfa
    Processing record 64 of 163|yar-sale
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=yar-sale
    Processing record 65 of 163|ferme-neuve
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ferme-neuve
    Processing record 66 of 163|salinas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=salinas
    Processing record 67 of 163|rikitea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea
    Processing record 68 of 163|saskylakh
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=saskylakh
    Processing record 69 of 163|vaini
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=vaini
    Processing record 70 of 163|albany
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=albany
    Processing record 71 of 163|nikolskoye
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=nikolskoye
    Processing record 72 of 163|tambacounda
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=tambacounda
    Processing record 73 of 163|hasaki
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hasaki
    Processing record 74 of 163|victoria
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria
    Processing record 75 of 163|tuktoyaktuk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=tuktoyaktuk
    Processing record 76 of 163|taolanaro
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=taolanaro
    Processing record 77 of 163|yellowknife
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=yellowknife
    Processing record 78 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 79 of 163|new norfolk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=new norfolk
    Processing record 80 of 163|amahai
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=amahai
    Processing record 81 of 163|vaini
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=vaini
    Processing record 82 of 163|sao jose da laje
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao jose da laje
    Processing record 83 of 163|klaksvik
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=klaksvik
    Processing record 84 of 163|albany
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=albany
    Processing record 85 of 163|yeppoon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=yeppoon
    Processing record 86 of 163|upernavik
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=upernavik
    Processing record 87 of 163|jumla
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=jumla
    Processing record 88 of 163|punta arenas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=punta arenas
    Processing record 89 of 163|freeport
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=freeport
    Processing record 90 of 163|yellowknife
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=yellowknife
    Processing record 91 of 163|hermanus
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hermanus
    Processing record 92 of 163|butaritari
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=butaritari
    Processing record 93 of 163|maragogi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=maragogi
    Processing record 94 of 163|santa vitoria do palmar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=santa vitoria do palmar
    Processing record 95 of 163|stawell
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=stawell
    Processing record 96 of 163|sault sainte marie
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=sault sainte marie
    Processing record 97 of 163|road town
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=road town
    Processing record 98 of 163|busselton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton
    Processing record 99 of 163|douglas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=douglas
    Processing record 100 of 163|petropavlovka
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=petropavlovka
    Processing record 101 of 163|faya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=faya
    Processing record 102 of 163|busselton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton
    Processing record 103 of 163|saskylakh
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=saskylakh
    Processing record 104 of 163|hermanus
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hermanus
    Processing record 105 of 163|wulanhaote
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=wulanhaote
    Processing record 106 of 163|rikitea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea
    Processing record 107 of 163|belushya guba
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=belushya guba
    Processing record 108 of 163|hilo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=hilo
    Processing record 109 of 163|barrow
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=barrow
    Processing record 110 of 163|elko
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=elko
    Processing record 111 of 163|bluff
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bluff
    Processing record 112 of 163|bluff
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bluff
    Processing record 113 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 114 of 163|yellowknife
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=yellowknife
    Processing record 115 of 163|bilibino
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bilibino
    Processing record 116 of 163|denau
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=denau
    Processing record 117 of 163|qarqin
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=qarqin
    Processing record 118 of 163|pacific grove
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=pacific grove
    Processing record 119 of 163|namibe
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=namibe
    Processing record 120 of 163|mys shmidta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=mys shmidta
    Processing record 121 of 163|victoria
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria
    Processing record 122 of 163|deputatskiy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=deputatskiy
    Processing record 123 of 163|rocha
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=rocha
    Processing record 124 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 125 of 163|beringovskiy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=beringovskiy
    Processing record 126 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 127 of 163|new norfolk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=new norfolk
    Processing record 128 of 163|omboue
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=omboue
    Processing record 129 of 163|busselton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton
    Processing record 130 of 163|coquimbo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=coquimbo
    Processing record 131 of 163|butaritari
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=butaritari
    Processing record 132 of 163|belushya guba
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=belushya guba
    Processing record 133 of 163|dakar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=dakar
    Processing record 134 of 163|immokalee
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=immokalee
    Processing record 135 of 163|rikitea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea
    Processing record 136 of 163|bluff
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=bluff
    Processing record 137 of 163|jamestown
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown
    Processing record 138 of 163|sola
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=sola
    Processing record 139 of 163|vallenar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=vallenar
    Processing record 140 of 163|lebu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=lebu
    Processing record 141 of 163|mataura
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=mataura
    Processing record 142 of 163|jamestown
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown
    Processing record 143 of 163|sao filipe
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao filipe
    Processing record 144 of 163|atar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=atar
    Processing record 145 of 163|narsaq
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=narsaq
    Processing record 146 of 163|ancud
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ancud
    Processing record 147 of 163|constitucion
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=constitucion
    Processing record 148 of 163|starobaltachevo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=starobaltachevo
    Processing record 149 of 163|lujiang
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=lujiang
    Processing record 150 of 163|sitka
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=sitka
    Processing record 151 of 163|inuvik
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=inuvik
    Processing record 152 of 163|ponta delgada
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta delgada
    Processing record 153 of 163|ushuaia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia
    Processing record 154 of 163|rikitea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea
    Processing record 155 of 163|ostrovnoy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=ostrovnoy
    Processing record 156 of 163|nyurba
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=nyurba
    Processing record 157 of 163|saint anthony
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint anthony
    Processing record 158 of 163|georgetown
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown
    Processing record 159 of 163|barvinkove
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=barvinkove
    Processing record 160 of 163|zeya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=zeya
    Processing record 161 of 163|punta arenas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=punta arenas
    Processing record 162 of 163|longyearbyen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb&q=longyearbyen
    163
    Data Retrieval Complete
    


```python
response_df = response_df.dropna(thresh = 3)
response_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>base</th>
      <th>clouds</th>
      <th>cod</th>
      <th>coord</th>
      <th>dt</th>
      <th>id</th>
      <th>main</th>
      <th>message</th>
      <th>name</th>
      <th>rain</th>
      <th>sys</th>
      <th>visibility</th>
      <th>weather</th>
      <th>wind</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>stations</td>
      <td>{'all': 90}</td>
      <td>200</td>
      <td>{'lon': -52.73, 'lat': 47.67}</td>
      <td>1.512842e+09</td>
      <td>6167817.0</td>
      <td>{'temp': 2, 'pressure': 1018, 'humidity': 93, ...</td>
      <td>NaN</td>
      <td>Torbay</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3467, 'message': 0.249, 'cou...</td>
      <td>24140.0</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3.1, 'deg': 260}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stations</td>
      <td>{'all': 56}</td>
      <td>200</td>
      <td>{'lon': 113.63, 'lat': -24.87}</td>
      <td>1.512845e+09</td>
      <td>2074865.0</td>
      <td>{'temp': 21.3, 'pressure': 1021.01, 'humidity'...</td>
      <td>NaN</td>
      <td>Carnarvon</td>
      <td>NaN</td>
      <td>{'message': 0.1847, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.21, 'deg': 291}</td>
    </tr>
    <tr>
      <th>4</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': 120.32, 'lat': 63.45}</td>
      <td>1.512845e+09</td>
      <td>2013639.0</td>
      <td>{'temp': -34.78, 'pressure': 1034.06, 'humidit...</td>
      <td>NaN</td>
      <td>Verkhnevilyuysk</td>
      <td>NaN</td>
      <td>{'message': 0.2984, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.61, 'deg': 243.5}</td>
    </tr>
    <tr>
      <th>5</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': -52.25, 'lat': -15.9}</td>
      <td>1.512845e+09</td>
      <td>3471840.0</td>
      <td>{'temp': 23.45, 'pressure': 969.22, 'humidity'...</td>
      <td>NaN</td>
      <td>Aragarcas</td>
      <td>{'3h': 6.765}</td>
      <td>{'message': 0.2028, 'country': 'BR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 501, 'main': 'Rain', 'description': 'm...</td>
      <td>{'speed': 2.96, 'deg': 269}</td>
    </tr>
    <tr>
      <th>6</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': -49.15, 'lat': -13.44}</td>
      <td>1.512845e+09</td>
      <td>3453014.0</td>
      <td>{'temp': 23.95, 'pressure': 963.87, 'humidity'...</td>
      <td>NaN</td>
      <td>Porangatu</td>
      <td>{'3h': 0.89}</td>
      <td>{'message': 0.2103, 'country': 'BR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 4.11, 'deg': 287}</td>
    </tr>
    <tr>
      <th>7</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 19.23, 'lat': -34.42}</td>
      <td>1.512845e+09</td>
      <td>3366880.0</td>
      <td>{'temp': 17.6, 'pressure': 993.62, 'humidity':...</td>
      <td>NaN</td>
      <td>Hermanus</td>
      <td>NaN</td>
      <td>{'message': 0.1968, 'country': 'ZA', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 5.66, 'deg': 109.5}</td>
    </tr>
    <tr>
      <th>8</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -175.2, 'lat': -21.2}</td>
      <td>1.512842e+09</td>
      <td>4032243.0</td>
      <td>{'temp': 24, 'pressure': 1009, 'humidity': 88,...</td>
      <td>NaN</td>
      <td>Vaini</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 8323, 'message': 0.1907, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 10.31, 'deg': 111.5}</td>
    </tr>
    <tr>
      <th>9</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': -155.09, 'lat': 19.73}</td>
      <td>1.512842e+09</td>
      <td>5855927.0</td>
      <td>{'temp': 15.34, 'pressure': 1016, 'humidity': ...</td>
      <td>NaN</td>
      <td>Hilo</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 818, 'message': 0.1813, 'cou...</td>
      <td>16093.0</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3.1, 'deg': 220}</td>
    </tr>
    <tr>
      <th>10</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 102.5, 'lat': 71.97}</td>
      <td>1.512845e+09</td>
      <td>2022572.0</td>
      <td>{'temp': -31.23, 'pressure': 1046.71, 'humidit...</td>
      <td>NaN</td>
      <td>Khatanga</td>
      <td>NaN</td>
      <td>{'message': 0.2063, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 4.81, 'deg': 78.0002}</td>
    </tr>
    <tr>
      <th>11</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': 11.22, 'lat': 42.44}</td>
      <td>1.512842e+09</td>
      <td>3171985.0</td>
      <td>{'temp': 2.93, 'pressure': 1011, 'humidity': 1...</td>
      <td>NaN</td>
      <td>Orbetello</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 5840, 'message': 0.1739, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 7.7, 'deg': 20}</td>
    </tr>
    <tr>
      <th>12</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': -134.97, 'lat': -23.12}</td>
      <td>1.512845e+09</td>
      <td>4030556.0</td>
      <td>{'temp': 25.7, 'pressure': 1030.98, 'humidity'...</td>
      <td>NaN</td>
      <td>Rikitea</td>
      <td>NaN</td>
      <td>{'message': 0.179, 'country': 'PF', 'sunrise':...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.86, 'deg': 58.5002}</td>
    </tr>
    <tr>
      <th>13</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': 95.32, 'lat': 5.89}</td>
      <td>1.512845e+09</td>
      <td>1214026.0</td>
      <td>{'temp': 27.53, 'pressure': 1024.58, 'humidity...</td>
      <td>NaN</td>
      <td>Sabang</td>
      <td>NaN</td>
      <td>{'message': 0.1844, 'country': 'ID', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.66, 'deg': 103.5}</td>
    </tr>
    <tr>
      <th>14</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -51.72, 'lat': 64.18}</td>
      <td>1.512842e+09</td>
      <td>3421319.0</td>
      <td>{'temp': 2, 'pressure': 991, 'humidity': 84, '...</td>
      <td>NaN</td>
      <td>Nuuk</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4801, 'message': 0.1925, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.5, 'deg': 160}</td>
    </tr>
    <tr>
      <th>16</th>
      <td>stations</td>
      <td>{'all': 48}</td>
      <td>200</td>
      <td>{'lon': 128.87, 'lat': 71.69}</td>
      <td>1.512845e+09</td>
      <td>2015306.0</td>
      <td>{'temp': -25.88, 'pressure': 1035.6, 'humidity...</td>
      <td>NaN</td>
      <td>Tiksi</td>
      <td>NaN</td>
      <td>{'message': 0.1842, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.41, 'deg': 48.5002}</td>
    </tr>
    <tr>
      <th>18</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': 81.77, 'lat': 51.95}</td>
      <td>1.512845e+09</td>
      <td>1494331.0</td>
      <td>{'temp': -7.93, 'pressure': 1006.18, 'humidity...</td>
      <td>NaN</td>
      <td>Pospelikha</td>
      <td>NaN</td>
      <td>{'message': 0.0044, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.56, 'deg': 196.5}</td>
    </tr>
    <tr>
      <th>19</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': 147.33, 'lat': -42.88}</td>
      <td>1.512842e+09</td>
      <td>2163355.0</td>
      <td>{'temp': 16, 'pressure': 1013, 'humidity': 55,...</td>
      <td>NaN</td>
      <td>Hobart</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 8195, 'message': 0.1926, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 9.3, 'deg': 330}</td>
    </tr>
    <tr>
      <th>20</th>
      <td>stations</td>
      <td>{'all': 1}</td>
      <td>200</td>
      <td>{'lon': -159.32, 'lat': 22.08}</td>
      <td>1.512842e+09</td>
      <td>5848280.0</td>
      <td>{'temp': 17.62, 'pressure': 1016, 'humidity': ...</td>
      <td>NaN</td>
      <td>Kapaa</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 833, 'message': 0.1723, 'cou...</td>
      <td>16093.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 2.6, 'deg': 290}</td>
    </tr>
    <tr>
      <th>21</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 168.33, 'lat': -46.6}</td>
      <td>1.512845e+09</td>
      <td>2206939.0</td>
      <td>{'temp': 13.68, 'pressure': 1018.34, 'humidity...</td>
      <td>NaN</td>
      <td>Bluff</td>
      <td>{'3h': 4.61}</td>
      <td>{'message': 0.1692, 'country': 'NZ', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 501, 'main': 'Rain', 'description': 'm...</td>
      <td>{'speed': 10.96, 'deg': 269.5}</td>
    </tr>
    <tr>
      <th>22</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': 122.23, 'lat': -17.97}</td>
      <td>1.512842e+09</td>
      <td>2075720.0</td>
      <td>{'temp': 30, 'pressure': 1008, 'humidity': 79,...</td>
      <td>NaN</td>
      <td>Broome</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 8176, 'message': 0.2497, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.1, 'deg': 230}</td>
    </tr>
    <tr>
      <th>23</th>
      <td>stations</td>
      <td>{'all': 90}</td>
      <td>200</td>
      <td>{'lon': -89.67, 'lat': 21.28}</td>
      <td>1.512842e+09</td>
      <td>3521108.0</td>
      <td>{'temp': 22, 'pressure': 1023, 'humidity': 56,...</td>
      <td>NaN</td>
      <td>Progreso</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3996, 'message': 0.1736, 'co...</td>
      <td>8047.0</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.2, 'deg': 320}</td>
    </tr>
    <tr>
      <th>24</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': 44.93, 'lat': 43.7}</td>
      <td>1.512845e+09</td>
      <td>562086.0</td>
      <td>{'temp': -1.48, 'pressure': 1019.63, 'humidity...</td>
      <td>NaN</td>
      <td>Galyugayevskaya</td>
      <td>NaN</td>
      <td>{'message': 0.1827, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.71, 'deg': 120}</td>
    </tr>
    <tr>
      <th>26</th>
      <td>stations</td>
      <td>{'all': 64}</td>
      <td>200</td>
      <td>{'lon': 145.92, 'lat': -41.07}</td>
      <td>1.512845e+09</td>
      <td>2173125.0</td>
      <td>{'temp': 15.63, 'pressure': 1030.09, 'humidity...</td>
      <td>NaN</td>
      <td>Burnie</td>
      <td>NaN</td>
      <td>{'message': 0.0042, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 8.06, 'deg': 267}</td>
    </tr>
    <tr>
      <th>27</th>
      <td>stations</td>
      <td>{'all': 56}</td>
      <td>200</td>
      <td>{'lon': 113.63, 'lat': -24.87}</td>
      <td>1.512845e+09</td>
      <td>2074865.0</td>
      <td>{'temp': 21.3, 'pressure': 1021.01, 'humidity'...</td>
      <td>NaN</td>
      <td>Carnarvon</td>
      <td>NaN</td>
      <td>{'message': 0.1847, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.21, 'deg': 291}</td>
    </tr>
    <tr>
      <th>28</th>
      <td>stations</td>
      <td>{'all': 1}</td>
      <td>200</td>
      <td>{'lon': -106.31, 'lat': 42.87}</td>
      <td>1.512842e+09</td>
      <td>5820705.0</td>
      <td>{'temp': 1, 'pressure': 1029, 'humidity': 50, ...</td>
      <td>NaN</td>
      <td>Casper</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3071, 'message': 0.1744, 'co...</td>
      <td>16093.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 10.8, 'deg': 220}</td>
    </tr>
    <tr>
      <th>29</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -70.92, 'lat': -53.15}</td>
      <td>1.512842e+09</td>
      <td>3874787.0</td>
      <td>{'temp': 8, 'pressure': 994, 'humidity': 65, '...</td>
      <td>NaN</td>
      <td>Punta Arenas</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4642, 'message': 0.1809, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 11.3, 'deg': 250}</td>
    </tr>
    <tr>
      <th>30</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -68.3, 'lat': -54.8}</td>
      <td>1.512842e+09</td>
      <td>3833367.0</td>
      <td>{'temp': 8, 'pressure': 990, 'humidity': 61, '...</td>
      <td>NaN</td>
      <td>Ushuaia</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4754, 'message': 0.1855, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 9.8, 'deg': 230, 'gust': 18.5}</td>
    </tr>
    <tr>
      <th>31</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': 27.85, 'lat': 71.04}</td>
      <td>1.512845e+09</td>
      <td>778707.0</td>
      <td>{'temp': -4.18, 'pressure': 996.86, 'humidity'...</td>
      <td>NaN</td>
      <td>Mehamn</td>
      <td>NaN</td>
      <td>{'message': 0.1796, 'country': 'NO', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.71, 'deg': 135.5}</td>
    </tr>
    <tr>
      <th>32</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': -42.73, 'lat': -17.29}</td>
      <td>1.512845e+09</td>
      <td>3445912.0</td>
      <td>{'temp': 23.33, 'pressure': 939.71, 'humidity'...</td>
      <td>NaN</td>
      <td>Turmalina</td>
      <td>{'3h': 7.4}</td>
      <td>{'message': 0.1805, 'country': 'BR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 501, 'main': 'Rain', 'description': 'm...</td>
      <td>{'speed': 3.36, 'deg': 290.5}</td>
    </tr>
    <tr>
      <th>33</th>
      <td>stations</td>
      <td>{'all': 56}</td>
      <td>200</td>
      <td>{'lon': 156.12, 'lat': 50.68}</td>
      <td>1.512845e+09</td>
      <td>2121385.0</td>
      <td>{'temp': -0.08, 'pressure': 982.92, 'humidity'...</td>
      <td>NaN</td>
      <td>Severo-Kurilsk</td>
      <td>NaN</td>
      <td>{'message': 0.1891, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 10.96, 'deg': 271.5}</td>
    </tr>
    <tr>
      <th>35</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': -69.36, 'lat': 77.48}</td>
      <td>1.512845e+09</td>
      <td>3831208.0</td>
      <td>{'temp': -4.78, 'pressure': 976.68, 'humidity'...</td>
      <td>NaN</td>
      <td>Qaanaaq</td>
      <td>NaN</td>
      <td>{'message': 0.1736, 'country': 'GL', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 4.41, 'deg': 95.0002}</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>128</th>
      <td>stations</td>
      <td>{'all': 80}</td>
      <td>200</td>
      <td>{'lon': 9.26, 'lat': -1.57}</td>
      <td>1.512845e+09</td>
      <td>2396853.0</td>
      <td>{'temp': 26.55, 'pressure': 1022.55, 'humidity...</td>
      <td>NaN</td>
      <td>Omboue</td>
      <td>NaN</td>
      <td>{'message': 0.1809, 'country': 'GA', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3.06, 'deg': 239.5}</td>
    </tr>
    <tr>
      <th>129</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 115.33, 'lat': -33.65}</td>
      <td>1.512845e+09</td>
      <td>2075265.0</td>
      <td>{'temp': 20.58, 'pressure': 1023.44, 'humidity...</td>
      <td>NaN</td>
      <td>Busselton</td>
      <td>NaN</td>
      <td>{'message': 0.0032, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 4.36, 'deg': 150}</td>
    </tr>
    <tr>
      <th>130</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -71.34, 'lat': -29.95}</td>
      <td>1.512842e+09</td>
      <td>3893629.0</td>
      <td>{'temp': 18, 'pressure': 1015, 'humidity': 72,...</td>
      <td>NaN</td>
      <td>Coquimbo</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4666, 'message': 0.1772, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.7, 'deg': 280}</td>
    </tr>
    <tr>
      <th>131</th>
      <td>stations</td>
      <td>{'all': 64}</td>
      <td>200</td>
      <td>{'lon': 172.79, 'lat': 3.07}</td>
      <td>1.512845e+09</td>
      <td>2110227.0</td>
      <td>{'temp': 27.38, 'pressure': 1021.5, 'humidity'...</td>
      <td>NaN</td>
      <td>Butaritari</td>
      <td>{'3h': 1.8325}</td>
      <td>{'message': 0.1732, 'country': 'KI', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 3.61, 'deg': 107}</td>
    </tr>
    <tr>
      <th>133</th>
      <td>stations</td>
      <td>{'all': 8}</td>
      <td>200</td>
      <td>{'lon': -17.44, 'lat': 14.69}</td>
      <td>1.512842e+09</td>
      <td>2253354.0</td>
      <td>{'temp': 26, 'pressure': 1012, 'humidity': 54,...</td>
      <td>NaN</td>
      <td>Dakar</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 6165, 'message': 0.1739, 'co...</td>
      <td>3500.0</td>
      <td>[{'id': 761, 'main': 'Dust', 'description': 'd...</td>
      <td>{'speed': 5.7, 'deg': 360}</td>
    </tr>
    <tr>
      <th>134</th>
      <td>stations</td>
      <td>{'all': 90}</td>
      <td>200</td>
      <td>{'lon': -81.42, 'lat': 26.42}</td>
      <td>1.512844e+09</td>
      <td>4159553.0</td>
      <td>{'temp': 18.32, 'pressure': 1015, 'humidity': ...</td>
      <td>NaN</td>
      <td>Immokalee</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 659, 'message': 0.0051, 'cou...</td>
      <td>3219.0</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 3.6, 'deg': 330}</td>
    </tr>
    <tr>
      <th>135</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': -134.97, 'lat': -23.12}</td>
      <td>1.512845e+09</td>
      <td>4030556.0</td>
      <td>{'temp': 25.7, 'pressure': 1030.98, 'humidity'...</td>
      <td>NaN</td>
      <td>Rikitea</td>
      <td>NaN</td>
      <td>{'message': 0.179, 'country': 'PF', 'sunrise':...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.86, 'deg': 58.5002}</td>
    </tr>
    <tr>
      <th>136</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 168.33, 'lat': -46.6}</td>
      <td>1.512845e+09</td>
      <td>2206939.0</td>
      <td>{'temp': 13.68, 'pressure': 1018.34, 'humidity...</td>
      <td>NaN</td>
      <td>Bluff</td>
      <td>{'3h': 4.61}</td>
      <td>{'message': 0.1692, 'country': 'NZ', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 501, 'main': 'Rain', 'description': 'm...</td>
      <td>{'speed': 10.96, 'deg': 269.5}</td>
    </tr>
    <tr>
      <th>137</th>
      <td>stations</td>
      <td>{'all': 80}</td>
      <td>200</td>
      <td>{'lon': -5.72, 'lat': -15.94}</td>
      <td>1.512845e+09</td>
      <td>3370903.0</td>
      <td>{'temp': 20.48, 'pressure': 1027.09, 'humidity...</td>
      <td>NaN</td>
      <td>Jamestown</td>
      <td>NaN</td>
      <td>{'message': 0.1774, 'country': 'SH', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.71, 'deg': 122}</td>
    </tr>
    <tr>
      <th>138</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 167.55, 'lat': -13.88}</td>
      <td>1.512845e+09</td>
      <td>2134814.0</td>
      <td>{'temp': 27.3, 'pressure': 1018.34, 'humidity'...</td>
      <td>NaN</td>
      <td>Sola</td>
      <td>NaN</td>
      <td>{'message': 0.186, 'country': 'VU', 'sunrise':...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 3.31, 'deg': 142}</td>
    </tr>
    <tr>
      <th>139</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -70.76, 'lat': -28.57}</td>
      <td>1.512845e+09</td>
      <td>3868633.0</td>
      <td>{'temp': 24.6, 'pressure': 896.51, 'humidity':...</td>
      <td>NaN</td>
      <td>Vallenar</td>
      <td>NaN</td>
      <td>{'message': 0.1739, 'country': 'CL', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 1.31, 'deg': 268}</td>
    </tr>
    <tr>
      <th>140</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': -73.65, 'lat': -37.62}</td>
      <td>1.512845e+09</td>
      <td>3883457.0</td>
      <td>{'temp': 13.58, 'pressure': 1030.74, 'humidity...</td>
      <td>NaN</td>
      <td>Lebu</td>
      <td>NaN</td>
      <td>{'message': 0.1677, 'country': 'CL', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 9.86, 'deg': 190.5}</td>
    </tr>
    <tr>
      <th>142</th>
      <td>stations</td>
      <td>{'all': 80}</td>
      <td>200</td>
      <td>{'lon': -5.72, 'lat': -15.94}</td>
      <td>1.512845e+09</td>
      <td>3370903.0</td>
      <td>{'temp': 20.48, 'pressure': 1027.09, 'humidity...</td>
      <td>NaN</td>
      <td>Jamestown</td>
      <td>NaN</td>
      <td>{'message': 0.1774, 'country': 'SH', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.71, 'deg': 122}</td>
    </tr>
    <tr>
      <th>143</th>
      <td>stations</td>
      <td>{'all': 36}</td>
      <td>200</td>
      <td>{'lon': -24.5, 'lat': 14.9}</td>
      <td>1.512845e+09</td>
      <td>3374210.0</td>
      <td>{'temp': 25.7, 'pressure': 1015.18, 'humidity'...</td>
      <td>NaN</td>
      <td>Sao Filipe</td>
      <td>NaN</td>
      <td>{'message': 0.1763, 'country': 'CV', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.71, 'deg': 58.0002}</td>
    </tr>
    <tr>
      <th>144</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -13.05, 'lat': 20.52}</td>
      <td>1.512845e+09</td>
      <td>2381334.0</td>
      <td>{'temp': 22.93, 'pressure': 1000.26, 'humidity...</td>
      <td>NaN</td>
      <td>Atar</td>
      <td>NaN</td>
      <td>{'message': 0.1768, 'country': 'MR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 5.01, 'deg': 77.0002}</td>
    </tr>
    <tr>
      <th>145</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -46.05, 'lat': 60.92}</td>
      <td>1.512842e+09</td>
      <td>3421719.0</td>
      <td>{'temp': 7, 'pressure': 987, 'humidity': 39, '...</td>
      <td>NaN</td>
      <td>Narsaq</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4791, 'message': 0.2525, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 15.4, 'deg': 60}</td>
    </tr>
    <tr>
      <th>146</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': -73.82, 'lat': -41.87}</td>
      <td>1.512845e+09</td>
      <td>3899695.0</td>
      <td>{'temp': 13.7, 'pressure': 1027.5, 'humidity':...</td>
      <td>NaN</td>
      <td>Ancud</td>
      <td>{'3h': 0.305}</td>
      <td>{'message': 0.1647, 'country': 'CL', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 3.76, 'deg': 285}</td>
    </tr>
    <tr>
      <th>148</th>
      <td>stations</td>
      <td>{'all': 76}</td>
      <td>200</td>
      <td>{'lon': 55.92, 'lat': 56}</td>
      <td>1.512845e+09</td>
      <td>488881.0</td>
      <td>{'temp': -8.48, 'pressure': 1009.1, 'humidity'...</td>
      <td>NaN</td>
      <td>Starobaltachevo</td>
      <td>NaN</td>
      <td>{'message': 0.0035, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.11, 'deg': 331.5}</td>
    </tr>
    <tr>
      <th>150</th>
      <td>stations</td>
      <td>{'all': 90}</td>
      <td>200</td>
      <td>{'lon': -135.33, 'lat': 57.05}</td>
      <td>1.512842e+09</td>
      <td>5557293.0</td>
      <td>{'temp': 9.41, 'pressure': 1005, 'humidity': 7...</td>
      <td>NaN</td>
      <td>Sitka</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 160, 'message': 0.0046, 'cou...</td>
      <td>16093.0</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 8.7, 'deg': 120, 'gust': 12.3}</td>
    </tr>
    <tr>
      <th>151</th>
      <td>stations</td>
      <td>{'all': 90}</td>
      <td>200</td>
      <td>{'lon': -133.72, 'lat': 68.35}</td>
      <td>1.512843e+09</td>
      <td>5983607.0</td>
      <td>{'temp': -13.79, 'pressure': 1014, 'humidity':...</td>
      <td>NaN</td>
      <td>Inuvik</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3535, 'message': 0.1742, 'co...</td>
      <td>24140.0</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1, 'deg': 310}</td>
    </tr>
    <tr>
      <th>152</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': -25.67, 'lat': 37.73}</td>
      <td>1.512844e+09</td>
      <td>3372783.0</td>
      <td>{'temp': 19, 'pressure': 1030, 'humidity': 88,...</td>
      <td>NaN</td>
      <td>Ponta Delgada</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 5957, 'message': 0.177, 'cou...</td>
      <td>10000.0</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.1, 'deg': 190}</td>
    </tr>
    <tr>
      <th>153</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -68.3, 'lat': -54.8}</td>
      <td>1.512842e+09</td>
      <td>3833367.0</td>
      <td>{'temp': 8, 'pressure': 990, 'humidity': 61, '...</td>
      <td>NaN</td>
      <td>Ushuaia</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4754, 'message': 0.1855, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 9.8, 'deg': 230, 'gust': 18.5}</td>
    </tr>
    <tr>
      <th>154</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': -134.97, 'lat': -23.12}</td>
      <td>1.512845e+09</td>
      <td>4030556.0</td>
      <td>{'temp': 25.7, 'pressure': 1030.98, 'humidity'...</td>
      <td>NaN</td>
      <td>Rikitea</td>
      <td>NaN</td>
      <td>{'message': 0.179, 'country': 'PF', 'sunrise':...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.86, 'deg': 58.5002}</td>
    </tr>
    <tr>
      <th>155</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 39.51, 'lat': 68.05}</td>
      <td>1.512845e+09</td>
      <td>556268.0</td>
      <td>{'temp': -9.9, 'pressure': 997.43, 'humidity':...</td>
      <td>NaN</td>
      <td>Ostrovnoy</td>
      <td>NaN</td>
      <td>{'message': 0.1666, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 4.71, 'deg': 159.5}</td>
    </tr>
    <tr>
      <th>156</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': 118.33, 'lat': 63.28}</td>
      <td>1.512845e+09</td>
      <td>2018735.0</td>
      <td>{'temp': -33.95, 'pressure': 1029.52, 'humidit...</td>
      <td>NaN</td>
      <td>Nyurba</td>
      <td>NaN</td>
      <td>{'message': 0.0043, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.11, 'deg': 237.5}</td>
    </tr>
    <tr>
      <th>158</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': -14.42, 'lat': -7.93}</td>
      <td>1.512842e+09</td>
      <td>2411397.0</td>
      <td>{'temp': 25, 'pressure': 1012, 'humidity': 65,...</td>
      <td>NaN</td>
      <td>Georgetown</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 6728, 'message': 0.172, 'cou...</td>
      <td>10000.0</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.7, 'deg': 130}</td>
    </tr>
    <tr>
      <th>159</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': 37.02, 'lat': 48.91}</td>
      <td>1.512845e+09</td>
      <td>712794.0</td>
      <td>{'temp': 0.43, 'pressure': 1010.88, 'humidity'...</td>
      <td>NaN</td>
      <td>Barvinkove</td>
      <td>NaN</td>
      <td>{'message': 0.1743, 'country': 'UA', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.96, 'deg': 169.5}</td>
    </tr>
    <tr>
      <th>160</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': 127.27, 'lat': 53.75}</td>
      <td>1.512845e+09</td>
      <td>2012593.0</td>
      <td>{'temp': -33.38, 'pressure': 965, 'humidity': ...</td>
      <td>NaN</td>
      <td>Zeya</td>
      <td>NaN</td>
      <td>{'message': 0.0045, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.01, 'deg': 2.00018}</td>
    </tr>
    <tr>
      <th>161</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -70.92, 'lat': -53.15}</td>
      <td>1.512842e+09</td>
      <td>3874787.0</td>
      <td>{'temp': 8, 'pressure': 994, 'humidity': 65, '...</td>
      <td>NaN</td>
      <td>Punta Arenas</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4642, 'message': 0.1809, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 11.3, 'deg': 250}</td>
    </tr>
    <tr>
      <th>162</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': 15.64, 'lat': 78.22}</td>
      <td>1.512842e+09</td>
      <td>2729907.0</td>
      <td>{'temp': -4, 'pressure': 1016, 'humidity': 68,...</td>
      <td>NaN</td>
      <td>Longyearbyen</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 5326, 'message': 0.1774, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 8.7, 'deg': 130}</td>
    </tr>
  </tbody>
</table>
<p>143 rows × 14 columns</p>
</div>




```python
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

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Clouds</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Max Temp</th>
      <th>Wind_Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Torbay</td>
      <td>90</td>
      <td>CA</td>
      <td>1512864000</td>
      <td>100</td>
      <td>47.67</td>
      <td>-52.73</td>
      <td>33.80</td>
      <td>5.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carnarvon</td>
      <td>8</td>
      <td>AU</td>
      <td>1512866656</td>
      <td>98</td>
      <td>-24.87</td>
      <td>113.63</td>
      <td>73.00</td>
      <td>9.28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Verkhnevilyuysk</td>
      <td>24</td>
      <td>RU</td>
      <td>1512866659</td>
      <td>52</td>
      <td>63.45</td>
      <td>120.32</td>
      <td>-30.60</td>
      <td>5.93</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aragarcas</td>
      <td>88</td>
      <td>BR</td>
      <td>1512866660</td>
      <td>98</td>
      <td>-15.90</td>
      <td>-52.25</td>
      <td>72.37</td>
      <td>2.68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Porangatu</td>
      <td>80</td>
      <td>BR</td>
      <td>1512866661</td>
      <td>98</td>
      <td>-13.44</td>
      <td>-49.15</td>
      <td>71.92</td>
      <td>3.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_df = pd.DataFrame(clean_rd)
clean_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>base</th>
      <th>clouds</th>
      <th>cod</th>
      <th>coord</th>
      <th>dt</th>
      <th>id</th>
      <th>main</th>
      <th>name</th>
      <th>rain</th>
      <th>sys</th>
      <th>visibility</th>
      <th>weather</th>
      <th>wind</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>stations</td>
      <td>{'all': 90}</td>
      <td>200</td>
      <td>{'lon': -52.73, 'lat': 47.67}</td>
      <td>1512842400</td>
      <td>6167817</td>
      <td>{'temp': 2, 'pressure': 1018, 'humidity': 93, ...</td>
      <td>Torbay</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3467, 'message': 0.249, 'cou...</td>
      <td>24140.0</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3.1, 'deg': 260}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>stations</td>
      <td>{'all': 56}</td>
      <td>200</td>
      <td>{'lon': 113.63, 'lat': -24.87}</td>
      <td>1512845211</td>
      <td>2074865</td>
      <td>{'temp': 21.3, 'pressure': 1021.01, 'humidity'...</td>
      <td>Carnarvon</td>
      <td>NaN</td>
      <td>{'message': 0.1847, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.21, 'deg': 291}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': 120.32, 'lat': 63.45}</td>
      <td>1512845260</td>
      <td>2013639</td>
      <td>{'temp': -34.78, 'pressure': 1034.06, 'humidit...</td>
      <td>Verkhnevilyuysk</td>
      <td>NaN</td>
      <td>{'message': 0.2984, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.61, 'deg': 243.5}</td>
    </tr>
    <tr>
      <th>3</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': -52.25, 'lat': -15.9}</td>
      <td>1512845261</td>
      <td>3471840</td>
      <td>{'temp': 23.45, 'pressure': 969.22, 'humidity'...</td>
      <td>Aragarcas</td>
      <td>{'3h': 6.765}</td>
      <td>{'message': 0.2028, 'country': 'BR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 501, 'main': 'Rain', 'description': 'm...</td>
      <td>{'speed': 2.96, 'deg': 269}</td>
    </tr>
    <tr>
      <th>4</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': -49.15, 'lat': -13.44}</td>
      <td>1512845263</td>
      <td>3453014</td>
      <td>{'temp': 23.95, 'pressure': 963.87, 'humidity'...</td>
      <td>Porangatu</td>
      <td>{'3h': 0.89}</td>
      <td>{'message': 0.2103, 'country': 'BR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 4.11, 'deg': 287}</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
#creates and styles the temperature vs latitude plot

temp_plot = plt.scatter(temps_df['Lats'],temps_df['Temps'])
plt.title('City Latitude vs Max Temperature (12/9/17)')
plt.style.use('seaborn-dark')
plt.ylabel('Max Temperature (F)')
plt.xlabel('Latitude')
plt.grid()
plt.savefig('Lat_Temp.png')
plt.show()

```


![png](output_8_0.png)



```python
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
```


![png](output_9_0.png)



```python
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
```


![png](output_10_0.png)



```python
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
```


![png](output_11_0.png)

