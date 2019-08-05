# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:03:21 2019

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:33:31 2019

@author: Dell
"""

import concurrent.futures
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

#爬虫主体
def load_url(url,timeout):
    with request.urlopen(url,timeout=timeout) as conn:
        html=conn.read()
        soup = BeautifulSoup(html, 'lxml')
        rest=[]
        test=soup.find_all('h1',{'class':'lemon--h1__373c0__2ZHSL heading--h2__373c0__1TQtb alternate__373c0__1uacp'})[0].find('span',{'class':"lemon--span__373c0__3997G"}).text
        test2='No Results for '
        print(test,test2)
        if test2 in test:
            print('error')
            Dollarsign=np.nan
            Rnumber=np.nan
            Rate=np.nan
            Name=np.nan
            temp=[Name,Rate,Rnumber,Dollarsign]
            rest_info.append(temp)
            
            
        else:
          rest=np.nan
          rest = soup.find_all('h3',{'class':'lemon--h3__373c0__sQmiG heading--h3__373c0__1n4Of alternate__373c0__1uacp'})[1].find('a')
          rest2=rest.parent.parent.parent

       
          try:
              Name=rest.attrs["name"]
          except: Name=np.nan
          try:
              Rate=rest2.find('div',{'role':'img'}).attrs["aria-label"]
          except: Rate=np.nan
          try:
              Rnumber=rest2.find('span',{'class':'lemon--span__373c0__3997G text__373c0__2pB8f reviewCount__373c0__2r4xT text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_'}).text
          except: Rnumber=np.nan
          try:
              Dollarsign=rest2.find('span',{'class':'lemon--span__373c0__3997G text__373c0__2pB8f priceRange__373c0__2DY87 text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_ text-bullet--after__373c0__1ZHaA'}).text
          except: Dollarsign=np.nan
          print(Name,Rate,Rnumber,Dollarsign)
          temp=[Name,Rate,Rnumber,Dollarsign]
          rest_info.append(temp)
    

 
#提取餐馆名单并转码
rest_load=pd.read_csv(r'C:\Users\Dell\Desktop\RA\DollarSign-master\TorontoRW\toronto_summer2019.tsv',sep='\t',header=0)

rest_list=np.array(list(rest_load['name']))
print(rest_list)


rest_list_parse=rest_list


for i in np.arange(0,len(rest_list_parse),1):
    rest_list_parse[i]=parse.quote(rest_list_parse[i])
    
urllist=np.array([])
rest_info=[]
temp=[]


#创建URL名单
for i in np.arange(0,len(rest_list),1):
    url='https://www.yelp.com/search?find_desc='+rest_list_parse[i]+'&find_loc=Toronto%2C%20ON'
    urllist=np.append(urllist,url)
#开爬
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    future_to_url={executor.submit(load_url,url,5):url for url in urllist}


#保存    
df=pd.DataFrame(rest_info)
df.columns=['name','rate','number of reviews','dollarsign']
df.to_csv(r'C:\Users\Dell\Desktop\RA\DollarSign-master\TorontoRW\toronto_summer2019_yelpt.tsv',sep='\t')