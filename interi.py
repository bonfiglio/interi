# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import math
from pathlib import Path
primo = 0
interi = {}  # dizionario di numeri interi
pageindex = {}
#interi[0]={0:{}}
MAXXFILE = 10000 # numero max di interi per pagina ogni pagina è salvata in un file interiPAG.json
intPage = 0  # Contatore di pagine

maxintero = 0
my_file = Path('interi'+'.json')
if my_file.is_file():
    with open('interi.json') as data_file:
       pageindex = json.loads(data_file.read())
    data_file.close()
    MAXXFILE=  pageindex.get("0")
    intPage =pageindex.__len__()
    interi[intPage]={str(intPage):{}}
    maxintero=intPage*MAXXFILE


for x in range(maxintero, 1000000):
    print(x, end='-')
    masdiv= int(math.sqrt(x))
    el=2
    while x % el != 0 and  el<=masdiv:   #el<=x//2:
        el += 2 if el > 2 else 1
    if el > masdiv:
        interi[intPage][x]=primo
        print(primo)
        primo +=1
    else:   
        divisore= x//el
        el=str(el)
        intPage= divisore//MAXXFILE
        if intPage not in interi:
            with open('interi' + str(intPage) + '.json') as data_file:
                interi[intPage]=json.loads(data_file.read())
            data_file.close()
        dict2 = interi[divisore//MAXXFILE][str(divisore)]
        dict2 = dict2.copy() if type(dict2) is dict else {divisore:1}
        dict2[el] = 0 if el not in dict2 else dict2[el] +1
        intPage = pageindex.__len__()
        interi[intPage][x]=dict2   
    if x%MAXXFILE+1==MAXXFILE:  
        intPage=x//MAXXFILE
        with open('interi'+str(intPage)+'.json', 'w') as fp:
            interi[intPage][intPage+1]=primo-1
            json.dump(interi[intPage], fp,indent=4)
            intPage +=1
            pageindex[str(intPage)]=0
            interi[intPage]={str(intPage):primo}
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
    