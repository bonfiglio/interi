#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:07:24 2018

@author: developer
"""
pageindex={}
for i in range(0,10)
    pageindex[i]=interi.get(i).get(i)
# =============================================================================
# from pathlib import Path
# import json
# my_file = Path('interi0'+'.json')
# if my_file.is_file():
#     with open('interi0.json') as data_file:
#        interi = json.loads(data_file.read())
# 
# =============================================================================
def mcd ( a ,  b)  :
    ret=1
    afp= interi.get(str(a))
    bfp=interi.get(str(b))
    if type(afp) is dict and type(bfp) is dict:
         for key, value in afp.items():
            if bfp.__contains__(str(key)) and bfp.get(key)>value:
                value=bfp.get(key)
            bfp[key]=value  
         ret=1   
         for key, value in bfp.items():   
             ret *=pow(int(key),value)
    else:
        if type(bfp) is dict and bfp.__contains__(str(a)):
                ret = b
        else:
                ret= a*b
    return ret
aa=1
for x in range(2,2):
    aa=mcd(x,aa)
    print(x,aa)
    
k=1
pentagono={}
candidati={}
stop= True
while stop :
     v=k*(3*k-1)//2
     for key, value in pentagono.items():
        if pentagono.__contains__(v-key) :
          candidati[v+key]={v:key} 
     if candidati.__contains__(v):
        print(candidati.get(v))
        stop=False
     pentagono[v]=k
     k=k+1
    