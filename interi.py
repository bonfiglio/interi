# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import math
from pathlib import Path
primo = 3
primi= [0,1,2] # lista numeri primi
interi = {}  # dizionario di numeri interi
MAXXFILE = 10000 # numero max di interi per pagina ogni pagina è salvata in un file interiPAG.json
intPage = "0"  # Contatore di pagine

maxintero = 3
my_file = Path('genint.json')
if my_file.is_file():
    with open('genint.json') as data_file:
       pageindex = json.loads(data_file.read())
    maxintero = pageindex.__len__()-1
    intPage =str(maxintero)
    primi = pageindex[intPage]
    primo = pageindex[str(maxintero-1)]
    maxintero *= MAXXFILE
    interi[intPage]={str(maxintero):{}}

    data_file.close()
else:
    pageindex = {"0": 0}
    interi["0"] = {"0": 0, "1": 1, "2": 2}

for x in range(maxintero, 200*MAXXFILE):
    print(x, end='-')
    masdiv= int(math.sqrt(x))
    el=2
    while x % primi[el] != 0 and  primi[el]<=masdiv:   #el<=x//2:
        el += 1
    if primi[el] > masdiv:
        interi[intPage][str(x)]=primo
        print(primo)
        primi.append(x)
        primo +=1
    else:   
        divisore= x//primi[el]
        #el=str(el)
        intPage= str(divisore//MAXXFILE)
        if intPage not in interi:
            with open('genint' + intPage + '.json') as data_file:
                interi[intPage]=json.loads(data_file.read())
            data_file.close()
        dict2 = interi[intPage][str(divisore)]
        dict2 = dict2.copy() if type(dict2) is dict else {str(divisore):1}
        kel=str(primi[el])
        dict2[kel] = 1 if kel not in dict2 else dict2[kel] +1
        intPage = str(pageindex.__len__()-1)
        interi[intPage][str(x)]=dict2
    if x%MAXXFILE+1==MAXXFILE:  
        intPage=str(x//MAXXFILE)
        with open('genint'+intPage+'.json', 'w') as data_file:
            pageindex[intPage]=primo
            interi[intPage]["0"]=primo-1
            json.dump(interi[intPage], data_file,indent=4)
            data_file.close()
            intPage = str(pageindex.__len__())
            pageindex[intPage]=0
            interi[intPage]={"0":primo}
with open('genint.json', 'w') as data_file:
    pageindex[intPage] = primi
    json.dump(pageindex, data_file, indent=4)
    data_file.close()

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
    