# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
primo = 0
interi = {}  # dizionario di numeri interi
pageindex = {}
interi[0]={0:{}}
MAXXFILE = 10000 # numero max di interi per pagina ogni pagina è salvata in un file interiPAG.json
intPage = 0  # Contatore di pagine
from pathlib import Path
maxintero = 0
my_file = Path('interi'+'.json')
if my_file.is_file():
    with open('interi.json') as data_file:
       pageindex = json.loads(data_file.read())
    MAXXFILE=  pageindex.get("0")
    maxintero=pageindex.__len__()*MAXXFILE

for x in range(maxintero, 100000):
    print(x, end='-')
    el=2
    while x % el != 0 and el<=x//2:
        el += 1
    if el > x//2:
        interi[intPage][x]=primo
        print(primo)
        primo +=1
    else:   
        divisore= x//el
        if type(interi[divisore//MAXXFILE][divisore]) is dict:
            dict2 = interi[divisore//MAXXFILE].get(divisore).copy()         
        else:
            dict2 = {divisore:1}
        if el not in dict2:
             dict2[el]=1
        else:
             dict2[el] +=1
        interi[intPage][x]=dict2   
    if x%MAXXFILE+1==MAXXFILE:  
        intPage=x//MAXXFILE
        with open('interi'+str(intPage)+'.json', 'w') as fp:
            interi[intPage][intPage+1]=primo-1
            json.dump(interi[intPage], fp,indent=4)
            intPage +=1
            interi[intPage]={intPage:primo}
     #    interi.append({x:dict2})                
# =============================================================================
#     x +=1
#     if type(interi[x//2]) is dict:
#          dict2 = interi[x//2].copy()
#          if 2 not in dict2:
#              dict2[2]=1
#          else:
#              dict2[2] +=1
#          interi.append(dict2)
#     else:
#         interi.append({2:1,x//2:1})
# =============================================================================


#print(interi)
    