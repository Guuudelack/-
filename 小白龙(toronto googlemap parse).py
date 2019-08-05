# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:34:34 2019

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:54:40 2019

@author: Dell
"""
import requests
from bs4 import BeautifulSoup
from urllib import request
import re
import time
def strip(string):
    return re.sub('\s+', '', string)
import csv
import numpy as np
import pandas as pd
from numpy import *
from pandas import *
from urllib import parse
import json

rest_load=pd.read_csv(r'C:\Users\Dell\Desktop\RA\DollarSign-master\TorontoRW\toronto_summer2019.tsv',sep='\t',header=0)

rest_list=np.array(list(rest_load['name']))
rest_info=[]
urllist=np.array([])
for i in np.arange(0,len(rest_list),1):
    url= url='https://maps.googleapis.com/maps/api/place/autocomplete/json?input='+rest_list[i]+'&location=43.7181557,-79.5181401&types=establishment&radius=50000&key=AIzaSyCZopxa-FAaMGQjd4itQkiyuEO9YbIjqfc'
    urllist=np.append(urllist,url)
    
for url in urllist:
    r=requests.get(url)
    try:
        ID=np.array(r.json()['predictions'])[0]['place_id']
        url2='https://maps.googleapis.com/maps/api/place/details/json?placeid='+ID+'&fields=name,rating,user_ratings_total,price_level&key=AIzaSyCZopxa-FAaMGQjd4itQkiyuEO9YbIjqfc'
        r2=requests.get(url2)
        rest=r2.json()['result']
    
        try:
            Name=rest["name"]
        except: Name=np.nan
        try:
            Rate=rest["rating"]
        except: Rate=np.nan
        try:
            Rnumber=rest["user_ratings_total"]
        except: Rnumber=np.nan
        try:
           Dollarsign=rest["price_level"]
        except: Dollarsign=np.nan
        print(Name,Rate,Rnumber,Dollarsign)
        
        rest_info.append((Name,Rate,Rnumber,Dollarsign))
        
    except:
            Dollarsign=np.nan
            Rnumber=np.nan
            Rate=np.nan
            Name=np.nan
            rest_info.append((Name,Rate,Rnumber,Dollarsign))
    
df=pd.DataFrame(rest_info)
df.columns=['name','rate','number of reviews','dollarsign']
df.to_csv(r'C:\Users\Dell\Desktop\RA\DollarSign-master\TorontoRW\toronto_summer2019_gmap.tsv',sep='\t')
    



