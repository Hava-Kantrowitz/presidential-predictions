# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:06:02 2018

@author: havak
"""

import pandas as pd
import csv

PATH = 'C:\\Users\\havak\\Desktop\\StemData\\'

#Bush Data

#Bush Tally 2000

bushVote00 = 50456062

#Bush Tally 2004

bushVote04 = 60963281

#Indiv contributions pro Bush
indivProBush00 = pd.read_csv(PATH + 'indivs00bars.txt' , delimiter = '|,|' , engine = 'python')
indivProBush00length = indivProBush00.shape[0]
print(indivProBush00length)

for x in indivProBush00length,0:
    marker = indivProBush00.iloc[x,19]
    if ( (marker!= P00003335) or (marker!= C00360503) or (marker!= C00343509) or (marker!= C00346932) or (marker!=C00404343) or (marker!= C00386987) or (marker!= C00388579) or (marker!= C00406678) or (marker!= C00401760) or (marker!= C00401604) or (marker!= C00380782) or (marker!= C00373084) or (marker!= C00343566) or (marker!= C00352682) or (marker!= C00341834) or (marker!= C00355040) or (marker!= C00353763) or (marker!= C00353250) or (marker!= C00352948) or (marker!= C00354076) or (marker!= C90006818)):
        indivProBush00.drop(indivProBush00[x])
    else:
        indivProBush00.drop(indivProBush00[0:7],axis = 1)
        indivProBush00.drop(indivProBush00[1:16], axis = 1)
        indivProBush00.astype(int)
        
indivProBush04 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\indivs04.txt' , delimiter = '|,|' , engine = 'python')
indivProBush04length = indivProBush04.shape[0]
print(indivProBush04length)

for x in indivProBush04length,0:
    marker = indivProBush04.iloc[x,19]
    if ( (marker!= P00003335) or (marker!= C00360503) or (marker!= C00343509) or (marker!= C00346932) or (marker!= C00404343) or (marker!= C00386987) or (marker!= C00388579) or (marker!= C00406678) or (marker!= C00401760) or (marker!= C00401604) or (marker!= C00380782) or (marker!= C00373084) or (marker!= C00343566) or (marker!= C00352682) or (marker!= C00341834) or (marker!= C00355040) or (marker!= C00353763) or (marker!= C00353250) or (marker!= C00352948) or (marker!= C00354076) or (marker!= C90006818)):
        indivProBush04.drop(indivProBush04[x])
    else:
        indivProBush04.drop(indivProBush04[0:7],axis = 1)
        indivProBush04.drop(indivProBush04[1:16], axis = 1)
        indivProBush04.astype(int)


#Indiv contributions anti Bush

indivAntiBush00 = pd.read_csv(PATH + 'indivs00bars.txt' , delimiter = '|,|' , engine = 'python')
indivAntiBush00length = indivAntiBush00.shape[0]
print(indivAntiBush00length)

for x in indivAntiBush00length,0:
    marker = indivAntiBush00.iloc[x,19]
    if marker!= C00388249 or marker!= C00387621 or marker != C00390765 or marker != C00400648 or marker != C00405688 or marker != C00405134 or marker != C00400176 or marker != C00405902 or marker!= C00398289:
        indivAntiBush00.drop(indivAntiBush00[x])
    else:
        indivAntiBush00.drop(indivAntiBush00[0:7],axis = 1)
        indivAntiBush00.drop(indivAntiBush00[1:16], axis = 1)
        indivAntiBush00.astype(int)

indivAntiBush04 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\indivs04.txt' , delimiter = '|,|' , engine = 'python')
indivAntiBush04length = indivAntiBush04.shape[0]
print(indivAntiBush04length)

for x in indivAntiBush04length,0:
    marker = indivAntiBush04.iloc[x,19]
    if marker!= C00388249 or marker!= C00387621 or marker != C00390765 or marker != C00400648 or marker != C00405688 or marker != C00405134 or marker != C00400176 or marker != C00405902 or marker!= C00398289:
        indivAntiBush04.drop(indivAntiBush04[x])
    else:
        indivAntiBush04.drop(indivAntiBush04[0:7],axis = 1)
        indivAntiBush04.drop(indivAntiBush04[1:16], axis = 1)
        indivAntiBush04.astype(int)

#Pacs pro Bush

pacProBush00 = pd.read_csv(PATH + 'pacs00.txt' , delimiter = '|,|' , engine = 'python')
pacProBush00length = pacProBush00.shape[0]
print(pacProBush00length)

for x in pacProBush00length,0:
    marker = pacProBush00.iloc[x,19]
    if marker!= P00003335 or marker!= C00360503 or marker!= C00343509 or marker!= C00346932 or marker!=C00404343 or marker!= C00386987 or marker!= C00388579 or marker!= C00406678 or marker!= C00401760 or marker!= C00401604 or marker!= C00380782 or marker!= C00373084 or marker!= C00343566 or marker!= C00352682 or marker!= C00341834 or marker!= C00355040 or marker!= C00353763 or marker!= C00353250 or marker!= C00352948 or marker!= C00354076 or marker!= C90006818:
        pacProBush00.drop(pacProBush00[x])
    else:
        pacProBush00.drop(pacProBush00[0:3],axis = 1)
        pacProBush00.drop(pacProBush00[1:9], axis = 1)
        pacProBush00.astype(int)
        
pacProBush002 = pd.read_csv(PATH + 'pacs_other00.txt' , delimiter = '|,|' , engine = 'python')
pacProBush002length = pacProBush002.shape[0]
print(pacProBush002length)

for x in pacProBush002length,0:
    marker = pacProBush002.iloc[x,19]
    if marker!= P00003335 or marker!= C00360503 or marker!= C00343509 or marker!= C00346932 or marker!= C00404343 or marker!= C00386987 or marker!= C00388579 or marker!= C00406678 or marker!= C00401760 or marker!= C00401604 or marker!= C00380782 or marker!= C00373084 or marker!= C00343566 or marker!= C00352682 or marker!= C00341834 or marker!= C00355040 or marker!= C00353763 or marker!= C00353250 or marker!= C00352948 or marker!= C00354076 or marker!= C90006818:
        pacProBush002.drop(pacProBush002[x])
    else:
        pacProBush002.drop(pacProBush002[0:3],axis = 1)
        pacProBush002.drop(pacProBush002[1:9], axis = 1)
        pacProBush002.astype(int)
        
pacProBush04 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\pacs04.txt' , delimiter = '|,|' , engine = 'python')
pacProBush04length = pacProBush04.shape[0]
print(pacProBush04length)

for x in pacProBush04length,0:
    marker.iloc[x,19]
    if marker!= P00003335 or marker!= C00360503 or marker!= C00343509 or marker!= C00346932 or marker!=C00404343 or marker!= C00386987 or marker!= C00388579 or marker!= C00406678 or marker!= C00401760 or marker!= C00401604 or marker!= C00380782 or marker!= C00373084 or marker!= C00343566 or marker!= C00352682 or marker!= C00341834 or marker!= C00355040 or marker!= C00353763 or marker!= C00353250 or marker!= C00352948 or marker!= C00354076 or marker!= C90006818:
        pacProBush04.drop(pacProBush04[x])
    else:
        pacProBush04.drop(indivProBush04[0:3],axis = 1)
        pacProBush04.drop(pacProBush04[1:9], axis = 1)
        pacProBush04.astype(int)
        
pacProBush042 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\pacs_other04.txt' , delimiter = '|,|' , engine = 'python')
pacProBush042length = pacProBush042.shape[0]
print(pacProBush042length)

for x in pacProBush042length,0:
    marker.iloc[x,19]
    if marker!= P00003335 or marker!= C00360503 or marker!= C00343509 or marker!= C00346932 or marker!=C00404343 or marker!= C00386987 or marker!= C00388579 or marker!= C00406678 or marker!= C00401760 or marker!= C00401604 or marker!= C00380782 or marker!= C00373084 or marker!= C00343566 or marker!= C00352682 or marker!= C00341834 or marker!= C00355040 or marker!= C00353763 or marker!= C00353250 or marker!= C00352948 or marker!= C00354076 or marker!= C90006818:
        pacProBush042.drop(pacProBush042[x])
    else:
        pacProBush042.drop(indivProBush042[0:3],axis = 1)
        pacProBush042.drop(pacProBush042[1:9], axis = 1)
        pacProBush042.astype(int)

#Pacs anti Bush

pacAntiBush00 = pd.read_csv(PATH + 'pacs00.txt' , delimiter = '|,|' , engine = 'python')
pacAntiBush00length = pacAntiBush00.shape[0]
print(pacAntiBush00length)

for x in pacAntiBush00length,0:
    marker = pacAntiBush00.iloc[x,19]
    if marker!= C00388249 or marker!= C00387621 or marker != C00390765 or marker != C00400648 or marker != C00405688 or marker != C00405134 or marker != C00400176 or marker != C00405902 or marker!= C00398289:
        pacAntiBush00.drop(pacAntiBush00[x])
    else:
        pacAntiBush00.drop(pacAntiBush00[0:3],axis = 1)
        pacAntiBush00.drop(pacAntiBush00[1:9], axis = 1)
        pacAntiBush00.astype(int)
        
pacAntiBush002 = pd.read_csv(PATH + 'pacs_other00.txt' , delimiter = '|,|' , engine = 'python')
pacAntiBush002length = pacAntiBush002.shape[0]
print(pacAntiBush002length)

for x in pacAntiBush002length,0:
    marker = pacAntiBush002.iloc[x,19]
    if marker!= C00388249 or marker!= C00387621 or marker != C00390765 or marker != C00400648 or marker != C00405688 or marker != C00405134 or marker != C00400176 or marker != C00405902 or marker!= C00398289:
        pacAntiBush002.drop(pacAntiBush002[x])
    else:
        pacAntiBush002.drop(pacAntiBush002[0:3],axis = 1)
        pacAntiBush002.drop(pacAntiBush002[1:9], axis = 1)
        pacAntiBush002.astype(int)

pacAntiBush04 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\pacs04.txt' , delimiter = '|,|' , engine = 'python')
pacAntiBush04length = pacAntiBush04.shape[0]
print(pacAntiBush04length)

for x in pacAntiBush04length,0:
    marker = pacAntiBush04.iloc[x,19]
    if marker!= C00388249 or marker!= C00387621 or marker != C00390765 or marker != C00400648 or marker != C00405688 or marker != C00405134 or marker != C00400176 or marker != C00405902 or marker!= C00398289:
        pacAntiBush04.drop(pacAntiBush04[x])
    else:
        pacAntiBush04.drop(pacAntiBush04[0:3],axis = 1)
        pacAntiBush04.drop(pacAntiBush04[1:9], axis = 1)
        pacAntiBush04.astype(int)
        
pacAntiBush042 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\pacs_other04.txt' , delimiter = '|,|' , engine = 'python')
pacAntiBush042length = pacAntiBush042.shape[0]
print(pacAntiBush042length)

for x in pacAntiBush042length,0:
    marker = pacAntiBush042.iloc[x,19]
    if marker!= C00388249 or marker!= C00387621 or marker != C00390765 or marker != C00400648 or marker != C00405688 or marker != C00405134 or marker != C00400176 or marker != C00405902 or marker!= C00398289:
        pacAntiBush042.drop(pacAntiBush042[x])
    else:
        pacAntiBush042.drop(pacAntiBush042[0:3],axis = 1)
        pacAntiBush042.drop(pacAntiBush042[1:9], axis = 1)
        pacAntiBush042.astype(int)

#Gore Data

#Gore vote tally
        
goreVote00 = 50996582

#Indiv contributions pro Gore

indivProGore00 = pd.read_csv(PATH + 'indivs00bars.txt' , delimiter = '|,|' , engine = 'python')
indivProGore00length = indivProGore00.shape[0]
print(indivProGore00length)

for x in indivProGore00length,0:
    marker = indivProGore00.iloc[x,19]
    if marker!= P80000912 or marker!= C00360982 or marker!= C00342204 or marker!= C00342212 or marker != C00444141 or marker!= C00437038 or marker!= C00432468 or marker!= C00394734 or marker!= C00431387 or marker!= C00165753 or marker!= C00342287 or marker!= C00349134 or marker!= C00355057 or marker!= C00353995:
        indivProGore00.drop(indivProGore00[x])
    else:
        indivProGore00.drop(indivProGore00[0:7],axis = 1)
        indivProGore00.drop(indivProGore00[1:16], axis = 1)
        indivProGore00.astype(int)
        
#Indiv contributions anti Gore
    
#NO ANTI

#Pacs pro Gore

pacProGore00 = pd.read_csv(PATH + 'pacs00.txt' , delimiter = '|,|' , engine = 'python')
pacProGore00length = pacProGore00.shape[0]
print(pacProGore00length)

for x in pacProGore00length,0:
    marker = pacvProGore00.iloc[x,19]
    if marker!= P80000912 or marker!= C00360982 or marker!= C00342204 or marker!= C00342212 or marker != C00444141 or marker!= C00437038 or marker!= C00432468 or marker!= C00394734 or marker!= C00431387 or marker!= C00165753 or marker!= C00342287 or marker!= C00349134 or marker!= C00355057 or marker!= C00353995:
        pacProGore00.drop(pacProGore00[x])
    else:
        pacProGore00.drop(pacProGore00[0:3],axis = 1)
        pacProGore00.drop(pacProGore00[1:9], axis = 1)
        pacProGore00.astype(int)
        
pacProGore002 = pd.read_csv(PATH + 'pacs_other00.txt' , delimiter = '|,|' , engine = 'python')
pacProGore002length = pacProGore002.shape[0]
print(pacProGore002length)

for x in pacProGore002length,0:
    marker = pacvProGore002.iloc[x,19]
    if marker!= P80000912 or marker!= C00360982 or marker!= C00342204 or marker!= C00342212 or marker != C00444141 or marker!= C00437038 or marker!= C00432468 or marker!= C00394734 or marker!= C00431387 or marker!= C00165753 or marker!= C00342287 or marker!= C00349134 or marker!= C00355057 or marker!= C00353995:
        pacProGore002.drop(pacProGore002[x])
    else:
        pacProGore002.drop(pacProGore002[0:3],axis = 1)
        pacProGore002.drop(pacProGore002[1:9], axis = 1)
        pacProGore002.astype(int)

#Pacs anti Gore
        
#NO ANTI

#Kerry Data

#Kerry Tally 2004

kerryVote04 = 57355978

#Indiv contributions pro Kerry

indivProKerry04 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\indivs04.txt' , delimiter = '|,|' , engine = 'python')
indivProKerry04length = indivProKerry04.shape[0]
print(indivProKerry04length)

for x in indivProKerry04length,0:
    marker = indivProKerry04.iloc[x,19]
    if marker!= P80000235 or marker!= C00404160 or marker!= C00385070 or marker!= C00383653 or marker!= C00398198 or marker!= C00404780 or marker!= C00406785 or marker!= C00177147 or marker!= C00401935 or marker!= C00407320 or marker!= C00405845 or marker!= C00403501:
        indivProKerry04.drop(indivProKerry04[x])
    else:
        indivProKerry04.drop(indivProKerry04[0:7],axis = 1)
        indivProKerry04.drop(indivProKerry04[1:16], axis = 1)
        indivProKerry04.astype(int)

#Indiv contributions anti Kerry
        
#NO ANTI

#Pacs pro Kerry
        
pacProKerry04 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\pacs04.txt' , delimiter = '|,|' , engine = 'python')
pacProKerry04length = pacProKerry04.shape[0]
print(pacProKerry04length)

for x in pacProKerry04length,0:
    marker = pacProKerry04.iloc[x,19]
    if marker!= P80000235 or marker!= C00404160 or marker!= C00385070 or marker!= C00383653 or marker!= C00398198 or marker!= C00404780 or marker!= C00406785 or marker!= C00177147 or marker!= C00401935 or marker!= C00407320 or marker!= C00405845 or marker!= C00403501:
        pacProKerry04.drop(pacProKerry04[x])
    else:
        pacProKerry04.drop(pacProKerry04[0:3],axis = 1)
        pacProKerry04.drop(pacProKerry04[1:9], axis = 1)
        pacProKerry04.astype(int)
        
pacProKerry042 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data04\\pacs_other04.txt' , delimiter = '|,|' , engine = 'python')
pacProKerry042length = pacProKerry042.shape[0]
print(pacProKerry042length)

for x in pacProKerry042length,0:
    marker = pacProKerry042.iloc[x,19]
    if marker!= P80000235 or marker!= C00404160 or marker!= C00385070 or marker!= C00383653 or marker!= C00398198 or marker!= C00404780 or marker!= C00406785 or marker!= C00177147 or marker!= C00401935 or marker!= C00407320 or marker!= C00405845 or marker!= C00403501:
        pacProKerry042.drop(pacProKerry042[x])
    else:
        pacProKerry042.drop(pacProKerry042[0:3],axis = 1)
        pacProKerry042.drop(pacProKerry042[1:9], axis = 1)
        pacProKerry042.astype(int)

#Pacs anti Kerry

#NO ANTI

#Obama Data
        
#Obama Tally 2008

obamaVote08 = 69498516

#Obama Tally 2012

obamaVote12 = 58720700

#Indiv contributions pro Obama
        
indivProObama08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\indivs08.txt' , delimiter = '|,|' , engine = 'python')
indivProObama08length = indivProObama08.shape[0]
print(indivProObama08length)

for x in indivProObama08length,0:
    marker = indivProObama08.iloc[x,19]
    if marker!= P8003330 or marker!= C00462176 or marker!= C00584193 or marker!= C00431445 or marker!= C00451393 or marker!= C00455949 or marker!= C00526624 or marker!= C00494740 or marker!= C00522706 or marker!= C00446179 or marker!= C00411934 or marker!= C00455527 or marker!= C00432310 or marker!= C90010877 or marker!= C00451773 or marker!= C0044317 or marker!= C00449900 or marker!= C00455113 or marker!= C00444356:
        indivProObama08.drop(indivProObama08[x])
    else:
        indivProObama08.drop(indivProObama08[0:7],axis = 1)
        indivProObama08.drop(indivProObama08[1:16], axis = 1)
        indivProObama08.astype(int)
        
indivProObama12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\indivs12.txt' , delimiter = '|,|' , engine = 'python')
indivProObama12length = indivProObama12.shape[0]
print(indivProObama12length)

for x in indivProObama12length,0:
    marker = indivProObama12.iloc[x,19]
    if marker!= P8003330 or marker!= C00462176 or marker!= C00584193 or marker!= C00431445 or marker!= C00451393 or marker!= C00455949 or marker!= C00526624 or marker!= C00494740 or marker!= C00522706 or marker!= C00446179 or marker!= C00411934 or marker!= C00455527 or marker!= C00432310 or marker!= C90010877 or marker!= C00451773 or marker!= C0044317 or marker!= C00449900 or marker!= C00455113 or marker!= C00444356:
        indivProObama12.drop(indivProObama12[x])
    else:
        indivProObama12.drop(indivProObama12[0:7],axis = 1)
        indivProObama12.drop(indivProObama12[1:16], axis = 1)
        indivProObama12.astype(int)

#Indiv contributions anti Obama
        
indivAntiObama08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\indivs08.txt' , delimiter = '|,|' , engine = 'python')
indivAntiObama08length = indivAntiObama08.shape[0]
print(indivAntiObama08length)

for x in indivAntiObama08length,0:
    marker = indivAntiObama08.iloc[x,19]
    if marker!= C00496729 or marker!= C00518464 or marker!= C00479865 or marker!= C00524579 or marker!= C90010497:
        indivAntiObama08.drop(indivAntiObama08[x])
    else:
        indivAntiObama08.drop(indivAntiObama08[0:7],axis = 1)
        indivAntiObama08.drop(indivAntiObama08[1:16], axis = 1)
        indivAntiObama08.astype(int)
        
indivAntiObama12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\indivs12.txt' , delimiter = '|,|' , engine = 'python')
indivAntiObama12length = indivAntiObama12.shape[0]
print(indivAntiObama12length)

for x in indivAntiObama12length,0:
    marker = indivAntiObama12.iloc[x,19]
    if marker!= C00496729 or marker!= C00518464 or marker!= C00479865 or marker!= C00524579 or marker!= C90010497:
        indivAntiObama12.drop(indivAntiObama12[x])
    else:
        indivAntiObama12.drop(indivAntiObama12[0:7],axis = 1)
        indivAntiObama12.drop(indivAntiObama12[1:16], axis = 1)
        indivAntiObama12.astype(int)

#Pacs pro Obama
        
pacProObama08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs08.txt' , delimiter = '|,|' , engine = 'python')
pacProObama08length = pacProObama08.shape[0]
print(pacProObama08length)

for x in pacProObama08length,0:
    marker = pacProObama08.iloc[x,19]
    if marker!= P8003330 or marker!= C00462176 or marker!= C00584193 or marker!= C00431445 or marker!= C00451393 or marker!= C00455949 or marker!= C00526624 or marker!= C00494740 or marker!= C00522706 or marker!= C00446179 or marker!= C00411934 or marker!= C00455527 or marker!= C00432310 or marker!= C90010877 or marker!= C00451773 or marker!= C0044317 or marker!= C00449900 or marker!= C00455113 or marker!= C00444356:
        pacProObama08.drop(pacProObama08[x])
    else:
        pacProObama08.drop(pacProObama08[0:3],axis = 1)
        pacProObama08.drop(pacProObama08[1:9], axis = 1)
        pacProObama08.astype(int)
        
pacProObama082 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs_other08.txt' , delimiter = '|,|' , engine = 'python')
pacProObama082length = pacProObama082.shape[0]
print(pacProObama082length)

for x in pacProObama082length,0:
    marker = pacProObama082.iloc[x,19]
    if marker!= P8003330 or marker!= C00462176 or marker!= C00584193 or marker!= C00431445 or marker!= C00451393 or marker!= C00455949 or marker!= C00526624 or marker!= C00494740 or marker!= C00522706 or marker!= C00446179 or marker!= C00411934 or marker!= C00455527 or marker!= C00432310 or marker!= C90010877 or marker!= C00451773 or marker!= C0044317 or marker!= C00449900 or marker!= C00455113 or marker!= C00444356:
        pacProObama082.drop(pacProObama082[x])
    else:
        pacProObama082.drop(pacProObama082[0:3],axis = 1)
        pacProObama082.drop(pacProObama082[1:9], axis = 1)
        pacProObama082.astype(int)
        
pacProObama12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs12.txt' , delimiter = '|,|' , engine = 'python')
pacProObama12length = pacProObama12.shape[0]
print(pacProObama12length)

for x in pacProObama12length,0:
    marker = pacProObama12.iloc[x,19]
    if marker!= P8003330 or marker!= C00462176 or marker!= C00584193 or marker!= C00431445 or marker!= C00451393 or marker!= C00455949 or marker!= C00526624 or marker!= C00494740 or marker!= C00522706 or marker!= C00446179 or marker!= C00411934 or marker!= C00455527 or marker!= C00432310 or marker!= C90010877 or marker!= C00451773 or marker!= C0044317 or marker!= C00449900 or marker!= C00455113 or marker!= C00444356:
        pacProObama12.drop(pacProObama12[x])
    else:
        pacProObama12.drop(pacProObama12[0:3],axis = 1)
        pacProObama12.drop(pacProObama12[1:9], axis = 1)
        pacProObama12.astype(int)
        
pacProObama122 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs_other12.txt' , delimiter = '|,|' , engine = 'python')
pacProObama122length = pacProObama122.shape[0]
print(pacProObama122length)

for x in pacProObama122length,0:
    marker = pacProObama122.iloc[x,19]
    if marker!= P8003330 or marker!= C00462176 or marker!= C00584193 or marker!= C00431445 or marker!= C00451393 or marker!= C00455949 or marker!= C00526624 or marker!= C00494740 or marker!= C00522706 or marker!= C00446179 or marker!= C00411934 or marker!= C00455527 or marker!= C00432310 or marker!= C90010877 or marker!= C00451773 or marker!= C0044317 or marker!= C00449900 or marker!= C00455113 or marker!= C00444356:
        pacProObama122.drop(pacProObama122[x])
    else:
        pacProObama122.drop(pacProObama122[0:3],axis = 1)
        pacProObama122.drop(pacProObama122[1:9], axis = 1)
        pacProObama122.astype(int)

#Pacs anti Obama

pacAntiObama08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs08.txt' , delimiter = '|,|' , engine = 'python')
pacAntiObama08length = pacAntiObama08.shape[0]
print(pacAntiObama08length)

for x in pacAntiObama08length,0:
    marker = pacAntiObama08.iloc[x,19]
    if marker!= C00496729 or marker!= C00518464 or marker!= C00479865 or marker!= C00524579 or marker!= C90010497:
        pacAntiObama08.drop(pacAntiObama08[x])
    else:
        pacAntiObama08.drop(pacAntiObama08[0:3],axis = 1)
        pacAntiObama08.drop(pacAntiObama08[1:9], axis = 1)
        pacAntiObama08.astype(int)
        
pacAntiObama082 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs_other08.txt' , delimiter = '|,|' , engine = 'python')
pacAntiObama082length = pacAntiObama082.shape[0]
print(pacAntiObama082length)

for x in pacAntiObama082length,0:
    marker = pacAntiObama082.iloc[x,19]
    if marker!= C00496729 or marker!= C00518464 or marker!= C00479865 or marker!= C00524579 or marker!= C90010497:
        pacAntiObama082.drop(pacAntiObama082[x])
    else:
        pacAntiObama082.drop(pacAntiObama082[0:3],axis = 1)
        pacAntiObama082.drop(pacAntiObama082[1:9], axis = 1)
        pacAntiObama082.astype(int)
        
pacAntiObama12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs12.txt' , delimiter = '|,|' , engine = 'python')
pacAntiObama12length = pacAntiObama12.shape[0]

for x in pacAntiObama12length,0:
    marker = pacAntiObama12.iloc[x,19]
    if marker!= C00496729 or marker!= C00518464 or marker!= C00479865 or marker!= C00524579 or marker!= C90010497:
        pacAntiObama12.drop(pacAntiObama12[x])
    else:
        pacAntiObama12.drop(pacAntiObama12[0:3],axis = 1)
        pacAntiObama12.drop(pacAntiObama12[1:9], axis = 1)
        pacAntiObama12.astype(int)
        
pacAntiObama122 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs_other12.txt' , delimiter = '|,|' , engine = 'python')
pacAntiObama122length = pacAntiObama122.shape[0]

for x in pacAntiObama122length,0:
    marker = pacAntiObama122.iloc[x,19]
    if marker!= C00496729 or marker!= C00518464 or marker!= C00479865 or marker!= C00524579 or marker!= C90010497:
        pacAntiObama122.drop(pacAntiObama122[x])
    else:
        pacAntiObama122.drop(pacAntiObama122[0:3],axis = 1)
        pacAntiObama122.drop(pacAntiObama122[1:9], axis = 1)
        pacAntiObama122.astype(int)

#Romney Data
        
#Romney Vote Tally
        
romneyVote12 = 56145950

#Indiv contributions pro Romney
        
indivProRomney12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\indivs12.txt' , delimiter = '|,|' , engine = 'python')
indivProRomney12length = indivProRomney12.shape[0]
print(indivProRomney12length)

for x in indivProRomney12length,0:
    marker = indivProRomney12.iloc[x,19]
    if marker!= P8003353 or marker!= C00660092 or marker!= C00431171 or marker!= C00518282 or marker!= C00571059 or marker!= C00519959 or marker!= C00528513 or marker!= C00502708:
        indivProRomney12.drop(indivProRomney12[x])
    else:
        indivProRomney12.drop(indivProRomney12[0:7],axis = 1)
        indivProRomney12.drop(indivProRomney12[1:16], axis = 1)
        indivProRomney12.astype(int)

#Indiv contributions anti Romney
        
indivAntiRomney12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\indivs12.txt' , delimiter = '|,|' , engine = 'python')
indivAntiRomney12length = indivAntiRomney12.shape[0]
print(indivAntiRomney12length)

for x in indivAntiRomneya12length,0:
    marker = indivAntiRomney12.iloc[x,19]
    if marker!= C00513598 or marker!= C00513572 or marker!= C00525832 or marker!= C00529859 or marker!= C00517284:
        indivAntiRomney12.drop(indivAntiRomney12[x])
    else:
        indivAntiRomney12.drop(indivAntiRomney12[0:7],axis = 1)
        indivAntiRomney12.drop(indivAntiRomney12[1:16], axis = 1)
        indivAntiRomney12.astype(int)

#Pacs pro Romney
        
pacProRomney12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs12.txt' , delimiter = '|,|' , engine = 'python')
pacProRomney12length = pacProRomney12.shape[0]
print(pacProRomney12length)

for x in pacProRomney12length,0:
    marker = pacProRomney12.iloc[x,19]
    if marker!= P8003353 or marker!= C00660092 or marker!= C00431171 or marker!= C00518282 or marker!= C00571059 or marker!= C00519959 or marker!= C00528513 or marker!= C00502708:
        pacProRomney12.drop(pacProRomney12[x])
    else:
        pacProRomney12.drop(pacProRomney12[0:3],axis = 1)
        pacProRomney12.drop(pacProRomney12[1:9], axis = 1)
        pacProRomney12.astype(int)
        
pacProRomney122 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs_other12.txt' , delimiter = '|,|' , engine = 'python')
pacProRomney122length = pacProRomney122.shape[0]
print(pacProRomney122length)

for x in pacProRomney122length,0:
    marker = pacProRomney122.iloc[x,19]
    if marker!= P8003353 or marker!= C00660092 or marker!= C00431171 or marker!= C00518282 or marker!= C00571059 or marker!= C00519959 or marker!= C00528513 or marker!= C00502708:
        pacProRomney122.drop(pacProRomney122[x])
    else:
        pacProRomney122.drop(pacProRomney122[0:3],axis = 1)
        pacProRomney122.drop(pacProRomney122[1:9], axis = 1)
        pacProRomney122.astype(int)

#Pacs anti Romney
        
pacAntiRomney12 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs12.txt' , delimiter = '|,|' , engine = 'python')
pacAntiRomney12length = pacAntiRomney12.shape[0]
print(pacAntiRomney12length)

for x in pacAntiRomneya12length,0:
    marker = pacAntiRomney12.iloc[x,19]
    if marker!= C00513598 or marker!= C00513572 or marker!= C00525832 or marker!= C00529859 or marker!= C00517284:
        pacAntiRomney12.drop(pacAntiRomney12[x])
    else:
        pacAntiRomney12.drop(pacAntiRomney12[0:3],axis = 1)
        pacAntiRomney12.drop(pacAntiRomney12[1:9], axis = 1)
        pacAntiRomney12.astype(int)
        
pacAntiRomney122 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data12\\pacs_other12.txt' , delimiter = '|,|' , engine = 'python')
pacAntiRomney122length = pacAntiRomney122.shape[0]
print(pacAntiRomney122length)

for x in pacAntiRomneya122length,0:
    marker = pacAntiRomney122.iloc[x,19]
    if marker!= C00513598 or marker!= C00513572 or marker!= C00525832 or marker!= C00529859 or marker!= C00517284:
        pacAntiRomney122.drop(pacAntiRomney122[x])
    else:
        pacAntiRomney122.drop(pacAntiRomney122[0:3],axis = 1)
        pacAntiRomney122.drop(pacAntiRomney122[1:9], axis = 1)
        pacAntiRomney122.astype(int)

#Mccain Data
        
#McCain Tally 2008
        
mccainVote08 = 59948323

#Indiv contributions pro Mccain
        
indivProMccain08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\indivs08.txt' , delimiter = '|,|' , engine = 'python')
indivProMccain08length = indivProMccain08.shape[0]
print(indivProMccain08length)

for x in indivProMccain08length,0:
    marker = indivProMccain08.iloc[x,19]
    if marker!= P8002801 or marker!= C00623207 or marker!= C00616607 or marker!= C00608497 or marker!= C00430470 or marker!= C00448498 or marker!= C00448985 or marker!= C00448878 or marker!= C00448860 or marker!= C00453928 or marker!= C00446104 or marker!= C00453738 or marker!= C00453951 or marker!= C00453878 or marker!= C00446682 or marker!= C00447417 or marker!= C00458802 or marker!= C00453969 or marker!= C00425454:
        indivProMccain08.drop(indivProMccain08[x])
    else:
        indivProMccain08.drop(indivProMccain08[0:7],axis = 1)
        indivProMccain08.drop(indivProMccain08[1:16], axis = 1)
        indivProMccain08.astype(int)

#Indiv contributions anti Mccain

indivAntiMccain08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\indivs08.txt' , delimiter = '|,|' , engine = 'python')
indivAntiMccain08length = indivAntiMccain08.shape[0]
print(indivAntiMccain08length)

for x in indivAntiMccain08length,0:
    marker = indivAntiMccain08.iloc[x,19]
    if marker!= C00432773:
        indivAntiMccain08.drop(indivAntiMccain08[x])
    else:
        indivAntiMccain08.drop(indivAntiMccain08[0:7],axis = 1)
        indivAntiMccain08.drop(indivAntiMccain08[1:16], axis = 1)
        indivAntiMccain08.astype(int)
        
#Pacs pro Mccain
        
pacProMccain08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs08.txt' , delimiter = '|,|' , engine = 'python')
pacProMccain08length = pacProMccain08.shape[0]
print(pacProMccain08length)

for x in pacProMccain08length,0:
    marker = pacProMccain08.iloc[x,19]
    if marker!= P8002801 or marker!= C00623207 or marker!= C00616607 or marker!= C00608497 or marker!= C00430470 or marker!= C00448498 or marker!= C00448985 or marker!= C00448878 or marker!= C00448860 or marker!= C00453928 or marker!= C00446104 or marker!= C00453738 or marker!= C00453951 or marker!= C00453878 or marker!= C00446682 or marker!= C00447417 or marker!= C00458802 or marker!= C00453969 or marker!= C00425454:
        pacProMccain08.drop(pacProMccain08[x])
    else:
        pacProMccain08.drop(pacProMccain08[0:3],axis = 1)
        pacProMccain08.drop(pacProMccain08[1:9], axis = 1)
        pacProMccain08.astype(int)
        
pacProMccain082 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs_other08.txt' , delimiter = '|,|' , engine = 'python')
pacProMccain082length = pacProMccain082.shape[0]
print(pacProMccain082length)

for x in pacProMccain082length,0:
    marker = pacProMccain082.iloc[x,19]
    if marker!= P8002801 or marker!= C00623207 or marker!= C00616607 or marker!= C00608497 or marker!= C00430470 or marker!= C00448498 or marker!= C00448985 or marker!= C00448878 or marker!= C00448860 or marker!= C00453928 or marker!= C00446104 or marker!= C00453738 or marker!= C00453951 or marker!= C00453878 or marker!= C00446682 or marker!= C00447417 or marker!= C00458802 or marker!= C00453969 or marker!= C00425454:
        pacProMccain082.drop(pacProMccain082[x])
    else:
        pacProMccain082.drop(pacProMccain082[0:3],axis = 1)
        pacProMccain082.drop(pacProMccain082[1:9], axis = 1)
        pacProMccain082.astype(int)

#Pacs anti Mccain
        
pacAntiMccain08 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs08.txt' , delimiter = '|,|' , engine = 'python')
pacAntiMccain08length = pacAntiMccain08.shape[0]
print(pacAntiMccain08length)

for x in pacAntiMccain08length,0:
    marker = pacAntiMccain08.iloc[x,19]
    if marker!= C00432773:
        pacAntiMccain08.drop(pacAntiMccain08[x])
    else:
        pacAntiMccain08.drop(pacAntiMccain08[0:3],axis = 1)
        pacAntiMccain08.drop(pacAntiMccain08[1:9], axis = 1)
        pacAntiMccain08.astype(int)
        
pacAntiMccain082 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data08\\pacs_other08.txt' , delimiter = '|,|' , engine = 'python')
pacAntiMccain082length = pacAntiMccain082.shape[0]
print(pacAntiMccain082length)

for x in pacAntiMccain082length,0:
    marker = pacAntiMccain082.iloc[x,19]
    if marker!= C00432773:
        pacAntiMccain082.drop(pacAntiMccain082[x])
    else:
        pacAntiMccain082.drop(pacAntiMccain082[0:3],axis = 1)
        pacAntiMccain082.drop(pacAntiMccain082[1:9], axis = 1)
        pacAntiMccain082.astype(int)

#Clinton Data
        
#Clinton Vote Tally
        
clintonVote16 = 65844310

#Indiv contributions pro Clinton
        
indivProClinton16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\indivs16.txt' , delimiter = '|,|' , engine = 'python')
indivProClinton16length = indivProClinton16.shape[0]
print(indivProClinton16length)

for x in indivProClinton16length,0:
    marker = indivProClinton16.iloc[x,19]
    if marker!= P00003392 or marker!= C00358895 or marker!= C00619411 or marker!= C00575795 or marker!= C00586537 or marker!= C00631408 or marker!= C00631408 or marker!= C00586818 or marker!= C00620435 or marker!= C00628537 or marker!= C00621961 or marker!= C00579508 or marker!= C00611889 or marker!= C00570069 or marker!= C00578310 or marker!= C00556639 or marker!= C00546762 or marker!= C00540559 or marker!= C00542290 or marker!= C00549832 or marker!= C00570846 or marker!= C00548610:
        indivProClinton16.drop(indivProClinton16[x])
    else:
        indivProClinton16.drop(indivProClinton16[0:7],axis = 1)
        indivProClinton16.drop(indivProClinton16[1:16], axis = 1)
        indivProClinton16.astype(int) 

#Indiv contributions anti Clinton
        
indivAntiClinton16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\indivs16.txt' , delimiter = '|,|' , engine = 'python')
indivAntiClinton16length = indivAntiClinton16.shape[0]
print(indivAntiClinton16length)

for x in indivAntiClinton16length,0:
    marker = indivAntiClinton16.iloc[x,19]
    if marker!= C00617084 or marker!= C00624122 or marker!= C00618058 or marker!= C00549840 or marker!= C00549832 or marker!= C00570630 or marker!= C00566968 or marker!= C00542829 or marker!= C00436501 or marker!= C00364257 or marker!= C00361394:
        indivAntiClinton16.drop(indivAntiClinton16[x])
    else:
        indivAntiClinton16.drop(indivAntiClinton16[0:7],axis = 1)
        indivAntiClinton16.drop(indivAntiClinton16[1:16], axis = 1)
        indivAntiClinton16.astype(int)

#Pacs pro Clinton
        
pacProClinton16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs16.txt' , delimiter = '|,|' , engine = 'python')
pacProClinton16length = pacProClinton16.shape[0]
print(pacProClinton16length)

for x in pacProClinton16length,0:
    marker = pacProClinton16.iloc[x,19]
    if marker!= P00003392 or marker!= C00358895 or marker!= C00619411 or marker!= C00575795 or marker!= C00586537 or marker!= C00631408 or marker!= C00631408 or marker!= C00586818 or marker!= C00620435 or marker!= C00628537 or marker!= C00621961 or marker!= C00579508 or marker!= C00611889 or marker!= C00570069 or marker!= C00578310 or marker!= C00556639 or marker!= C00546762 or marker!= C00540559 or marker!= C00542290 or marker!= C00549832 or marker!= C00570846 or marker!= C00548610:
        pacProClinton16.drop(pacProClinton16[x])
    else:
        pacProClinton16.drop(pacProClinton16[0:3],axis = 1)
        pacProClinton16.drop(pacProClinton16[1:9], axis = 1)
        pacProClinton16.astype(int)
        
pacProClinton162 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs_other16.txt' , delimiter = '|,|' , engine = 'python')
pacProClinton162length = pacProClinton162.shape[0]
print(pacProClinton162length)

for x in pacProClinton162length,0:
    marker = pacProClinton162.iloc[x,19]
    if marker!= P00003392 or marker!= C00358895 or marker!= C00619411 or marker!= C00575795 or marker!= C00586537 or marker!= C00631408 or marker!= C00631408 or marker!= C00586818 or marker!= C00620435 or marker!= C00628537 or marker!= C00621961 or marker!= C00579508 or marker!= C00611889 or marker!= C00570069 or marker!= C00578310 or marker!= C00556639 or marker!= C00546762 or marker!= C00540559 or marker!= C00542290 or marker!= C00549832 or marker!= C00570846 or marker!= C00548610:
        pacProClinton162.drop(pacProClinton162[x])
    else:
        pacProClinton162.drop(pacProClinton162[0:3],axis = 1)
        pacProClinton162.drop(pacProClinton162[1:9], axis = 1)
        pacProClinton162.astype(int)

#Pacs anti Clinton
        
pacAntiClinton16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs16.txt' , delimiter = '|,|' , engine = 'python')
pacAntiClinton16length = pacAntiClinton16.shape[0]
print(pacAntiClinton16length)

for x in pacAntiClinton16length,0:
    marker = pacAntiClinton16.iloc[x,19]
    if marker!= C00617084 or marker!= C00624122 or marker!= C00618058 or marker!= C00549840 or marker!= C00549832 or marker!= C00570630 or marker!= C00566968 or marker!= C00542829 or marker!= C00436501 or marker!= C00364257 or marker!= C00361394:
        pacAntiClinton16.drop(pacAntiClinton16[x])
    else:
        pacAntiClinton16.drop(pacAntiClinton16[0:3],axis = 1)
        pacAntiClinton16.drop(pacAntiClinton16[1:9], axis = 1)
        pacAntiClinton16.astype(int)

pacAntiClinton162 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs_other16.txt' , delimiter = '|,|' , engine = 'python')
pacAntiClinton162length = pacAntiClinton162.shape[0]
print(pacAntiClinton162length)

for x in pacAntiClinton162length,0:
    marker = pacAntiClinton162.iloc[x,19]
    if marker!= C00617084 or marker!= C00624122 or marker!= C00618058 or marker!= C00549840 or marker!= C00549832 or marker!= C00570630 or marker!= C00566968 or marker!= C00542829 or marker!= C00436501 or marker!= C00364257 or marker!= C00361394:
        pacAntiClinton162.drop(pacAntiClinton162[x])
    else:
        pacAntiClinton162.drop(pacAntiClinton162[0:3],axis = 1)
        pacAntiClinton162.drop(pacAntiClinton162[1:9], axis = 1)
        pacAntiClinton162.astype(int)
        
#Trump Data
        
#Trump Tally 2016
        
trumpVote16 = 62979636

#Indiv contributions pro Trump
        
indivProTrump16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\indivs16.txt' , delimiter = '|,|' , engine = 'python')
indivProTrump16length = indivProTrump16.shape[0]
print(indivProTrump16length)

for x in indivProTrump16length,0:
    marker = indivProTrump16.iloc[x,19]
    if marker!= P8001571 or marker!= C00656082 or marker!= C00618959 or marker!= C00618421 or marker!= C00580100 or marker!= C00654020 or marker!= C00618371 or marker!= C00594564 or marker!= C00618389 or marker!= C00622159 or marker!= C00626705 or marker!= C00621672 or marker!= C90016668 or marker!= C0060591 or marker!= C00588319 or marker!= C00586826 or marker!= C00623645 or marker!= C00590398 or marker!= C90015728 or marker!= C00609073 or marker!= C00591008:
        indivProTrump16.drop(indivProTrump16[x])
    else:
        indivProTrump16.drop(indivProTrump16[0:7],axis = 1)
        indivProTrump16.drop(indivProTrump16[1:16], axis = 1)
        indivProTrump16.astype(int)

#Indiv contributions anti Trump
        
indivAntiTrump16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\indivs16.txt' , delimiter = '|,|' , engine = 'python')
indivAntiTrump16length = indivAntiTrump16.shape[0]
print(indivAntiTrump16length)

for x in indivAntiTrump16length,0:
    marker = indivAntiTrump16.iloc[x,19]
    if marker!= P60018991 or marker!= P60018835 or marker!= C00638395 or marker!= C00633875 or marker!= C00632844 or marker!= C00633032 or marker!= C00632489 or marker!= C00629113 or marker!= C00611160 or marker!= C00612853 or marker!= C00624650 or marker!= C00585836 or marker!= C00628779:
        indivAntiTrump16.drop(indivAntiTrump16[x])
    else:
        indivAntiTrump16.drop(indivAntiTrump16[0:7],axis = 1)
        indivAntiTrump16.drop(indivAntiTrump16[1:16], axis = 1)
        indivAntiTrump16.astype(int)

#Pacs pro Trump

pacProTrump16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs16.txt' , delimiter = '|,|' , engine = 'python')
pacProTrump16length = pacProTrump16.shape[0]
print(pacProTrump16length)

for x in pacProTrump16length,0:
    marker = pacProTrump16.iloc[x,19]
    if marker!= P8001571 or marker!= C00656082 or marker!= C00618959 or marker!= C00618421 or marker!= C00580100 or marker!= C00654020 or marker!= C00618371 or marker!= C00594564 or marker!= C00618389 or marker!= C00622159 or marker!= C00626705 or marker!= C00621672 or marker!= C90016668 or marker!= C0060591 or marker!= C00588319 or marker!= C00586826 or marker!= C00623645 or marker!= C00590398 or marker!= C90015728 or marker!= C00609073 or marker!= C00591008:
        pacProTrump16.drop(pacProTrump16[x])
    else:
        pacProTrump16.drop(pacProTrump16[0:3],axis = 1)
        pacProTrump16.drop(pacProTrump16[1:9], axis = 1)
        pacProTrump16.astype(int)
        
pacProTrump162 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs_other16.txt' , delimiter = '|,|' , engine = 'python')
pacProTrump162length = pacProTrump162.shape[0]
print(pacProTrump162length)

for x in pacProTrump162length,0:
    marker = pacProTrump162.iloc[x,19]
    if marker!= P8001571 or marker!= C00656082 or marker!= C00618959 or marker!= C00618421 or marker!= C00580100 or marker!= C00654020 or marker!= C00618371 or marker!= C00594564 or marker!= C00618389 or marker!= C00622159 or marker!= C00626705 or marker!= C00621672 or marker!= C90016668 or marker!= C0060591 or marker!= C00588319 or marker!= C00586826 or marker!= C00623645 or marker!= C00590398 or marker!= C90015728 or marker!= C00609073 or marker!= C00591008:
        pacProTrump162.drop(pacProTrump162[x])
    else:
        pacProTrump162.drop(pacProTrump162[0:3],axis = 1)
        pacProTrump162.drop(pacProTrump162[1:9], axis = 1)
        pacProTrump162.astype(int)

#Pacs anti Trump
        
pacAntiTrump16 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs16.txt' , delimiter = '|,|' , engine = 'python')
pacAntiTrump16length = pacAntiTrump16.shape[0]
print(pacAntiTrump16length)

for x in pacAntiTrump16length,0:
    marker = pacAntiTrump16.iloc[x,19]
    if marker!= P60018991 or marker!= P60018835 or marker!= C00638395 or marker!= C00633875 or marker!= C00632844 or marker!= C00633032 or marker!= C00632489 or marker!= C00629113 or marker!= C00611160 or marker!= C00612853 or marker!= C00624650 or marker!= C00585836 or marker!= C00628779:
        pacAntiTrump16.drop(pacAntiTrump16[x])
    else:
        pacAntiTrump16.drop(pacAntiTrump16[0:3],axis = 1)
        pacAntiTrump16.drop(pacAntiTrump16[1:9], axis = 1)
        pacAntiTrump16.astype(int)
        
pacAntiTrump162 = pd.read_csv('C:\\Users\\havak\\Desktop\\StemData\\Data16\\pacs_other16.txt' , delimiter = '|,|' , engine = 'python')
pacAntiTrump162length = pacAntiTrump162.shape[0]
print(pacAntiTrump162length)

for x in pacAntiTrump162length,0:
    marker = pacAntiTrump162.iloc[x,19]
    if marker!= P60018991 or marker!= P60018835 or marker!= C00638395 or marker!= C00633875 or marker!= C00632844 or marker!= C00633032 or marker!= C00632489 or marker!= C00629113 or marker!= C00611160 or marker!= C00612853 or marker!= C00624650 or marker!= C00585836 or marker!= C00628779:
        pacAntiTrump162.drop(pacAntiTrump162[x])
    else:
        pacAntiTrump162.drop(pacAntiTrump162[0:3],axis = 1)
        pacAntiTrump162.drop(pacAntiTrump162[1:9], axis = 1)
        pacAntiTrump162.astype(int)


import numpy as np
import matplotlib.pyplot as plt

#setting the data

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProBush00


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProBush00


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProGore00


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProGore00


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiBush00


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiBush00


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProBush04


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProBush04


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProKerry04


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProKerry04


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiBush04


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiBush04


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProObama08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProObama08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiMccain08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiMccain08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProMccain08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProMccain08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiObama08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiObama08


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProObama12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProObama12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiRomney12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiRomney12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProRomney12

# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProRomney12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiObama12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiObama12


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProTrump16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProTrump16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiClinton16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiClinton16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivProClinton16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacProClinton16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = indivAntiTrump16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = pacAntiTrump16


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)

print("Prediction:")