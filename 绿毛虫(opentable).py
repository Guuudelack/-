# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:55:46 2019

@author: Dell
"""


"""
Created on Tue Jul 23 10:33:31 2019

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
from urllib import parse,error

rest_load=pd.read_csv(r'C:\Users\Dell\Desktop\RA\DollarSign-master\TorontoRW\toronto_summer2019.tsv',sep='\t',header=0)

rest_list=np.array(list(rest_load['name']))
print(rest_list)

urllist=np.array([])
rest_info=[]



for i in np.arange(0,len(rest_list),1):
    url='https://www.opentable.com/s/?currentview=list&pinnedrids=116407&size=100&sort=PreSorted&covers=2&dateTime=2019-07-24+19%3A00&latitude=43.681182&longitude=-79.429227&metroId=74&regionIds=164&term='+rest_list[i]
    urllist=np.append(urllist,url)

for i in np.arange(0,len(rest_list),1):
        urluse = urllist[i]
        authority='www.opentable.com'
        method='GET'
        scheme='https'
        accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        accept2='gzip, deflate, br'
        cache2='max-age=0'
        none='W/"1f6c8-6s1O0xqtzJykZes8hu7QZtaS+bk"'
        upgrade='1'
        user='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        headers={"authority":authority,"method":method,"scheme":scheme,"accept":accept,"accept-encoding":accept2,"cache-control":cache2,"if-none-match":none,"upgrade-insecure-requests":upgrade,"user-agent":user}
        rsp=requests.get(urluse,headers=headers)
        html=rsp.text
        
        try:
            soup = BeautifulSoup(html, 'lxml')
            rest=[]
            test=soup.find_all('div',{'id':'search_results_container'})[0].find('div',{'class':"result content-section-list-row cf with-times"}).find('span',{'class':'rest-row-name-text'}).text
            test2=rest_list[i]
            print(test,test2)
            if test2 in test or test in test2:
              rest=np.nan
              rest = soup.find_all('div',{'class':'rest-row-info'})[0]
              
           
              try:
                  Name=test
              except: Name=np.nan
              try:
                  Rate=rest.find('div',{'class':'all-stars filled'})['style']
              except: Rate=np.nan
              try:
                  Rnumber=rest.find('span',{'class':'underline-hover'}).text
              except: Rnumber=np.nan
              try:
                 Dollarsign=rest.find('i',{'class':'pricing--the-price'}).text
              except: Dollarsign=np.nan
              print(Name,Rate,Rnumber,Dollarsign)
        
              rest_info.append((Name,Rate,Rnumber,Dollarsign))
               
                
            else:
              print('error')
              Dollarsign=np.nan
              Rnumber=np.nan
              Rate=np.nan
              Name=np.nan
              rest_info.append((Name,Rate,Rnumber,Dollarsign))
              continue
        except:
            print('error')
            Dollarsign=np.nan
            Rnumber=np.nan
            Rate=np.nan
            Name=np.nan
            rest_info.append((Name,Rate,Rnumber,Dollarsign))
           

    
df=pd.DataFrame(rest_info)
df.columns=['name','rate','number of reviews','dollarsign']
df.to_csv(r'C:\Users\Dell\Desktop\RA\DollarSign-master\TorontoRW\toronto_summer2019_op.tsv',sep='\t')