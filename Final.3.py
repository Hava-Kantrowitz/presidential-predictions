# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:07:51 2018

@author: havak
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:44:14 2018

@author: havak
"""

#Values given by Open Secrets election data Bayesian analysis

#Bush Data 2000
 
indivProBush00 = 271814028

pacProBush00 = 2917020

BushAssets00 = 19291233

#Gore Data 2000

indivProGore00 = 46840118 

pacProGore00 = 946012

GoreAssets00 = 12772827

# 2000 Math

Bush00indiv = abs(indivProBush00 - indivProGore00)
while Bush00indiv > 100:
    Bush00indiv = Bush00indiv/4

Bush00pac = abs(pacProBush00 - pacProGore00)
while Bush00pac > 100:
    Bush00pac = Bush00pac/4
    
Bush00asset = abs(BushAssets00 - GoreAssets00)
while Bush00asset > 100:
    Bush00asset = Bush00asset/4

Bush00prediction = (Bush00asset + Bush00pac + Bush00indiv)/3
print("BUSH VOTE PERCENTAGE 2000:")
print(Bush00prediction)

Gore00prediction = 100-Bush00prediction
print("GORE VOTE PERCENTAGE 2000:")
print(Gore00prediction)
    
#Bush Data 2004

indivProBush04 = 279215332

pacProBush04 = 2989594

BushAssets04 = 19291233

#Kerry Data 2004

indivProKerry001 = 3528052
indivProKerry002 = 7941576
indivProKerry04 = indivProKerry001 + indivProKerry002 

pacProKerry04 = 17200

KerryAssets04 = 2957582

# 2004 Math

Bush04indiv = abs(indivProBush04 - indivProKerry04)
while Bush04indiv > 100:
    Bush04indiv = Bush04indiv/4

Bush04pac = abs(pacProBush04 - pacProKerry04)
while Bush04pac > 100:
    Bush04pac = Bush04pac/4
    
Bush04asset = abs(BushAssets04 - KerryAssets04)
while Bush04asset > 100:
    Bush04asset = Bush04asset/4

Bush04prediction = (Bush04asset + Bush04pac + Bush04indiv)/3
print("BUSH VOTE PERCENTAGE 2004:")
print(Bush04prediction)

Gore04prediction = 100-Bush04prediction
print("KERRY VOTE PERCENTAGE 2004:")
print(Gore04prediction)

#McCain Data 2008

indivProMccain01 = 1680340
indivProMccain02 = 1839358
indivProMccain08 = indivProMccain01 + indivProMccain02

pacProMccain08 = 690393

MccainAssets08 = 2506882

#Obama Data 2008

indivProObama08 = 656357572

pacProObama08 = 1830	

ObamaAssets08 = 15466043

#2008 Math

Mccain08indiv = abs(indivProMccain08 - indivProObama08)
while Mccain08indiv > 100:
    Mccain08indiv = Mccain08indiv/4

Mccain08pac = abs(pacProMccain08 - pacProObama08)
while Mccain08pac > 100:
    Mccain08pac = Mccain08pac/4
    
Mccain08asset = abs(MccainAssets08 - ObamaAssets08)
while Mccain08asset > 100:
    Mccain08asset = Mccain08asset/4

Mccain08prediction = (Mccain08asset + Mccain08pac + Mccain08indiv)/3
print("MCCAIN VOTE PERCENTAGE 2008:")
print(Mccain08prediction)

Obama08prediction = 100-Mccain08prediction
print("OBAMA VOTE PERCENTAGE 2008:")
print(Obama08prediction)

#Romney Data 2012

indivProRomney12 = 300019783

pacProRomney12 = 1092055	

RomneyAssets12 = 449886513

#Obama Data 2012

indivProObama12 = 549580640

pacProObama12 = 	5000

ObamaAssets12 = 3301800

#2012 Math

Romney12indiv = abs(indivProRomney12 - indivProObama12)
while Romney12indiv > 100:
    Romney12indiv = Romney12indiv/4

Romney12pac = abs(pacProRomney12 - pacProObama12)
while Romney12pac > 100:
    Romney12pac = Romney12pac/4
    
Romney12asset = abs(RomneyAssets12 - ObamaAssets12)
while Romney12asset > 100:
    Romney12asset = Romney12asset/4

Romney12prediction = (Romney12asset + Romney12pac + Romney12indiv)/3
print("ROMNEY VOTE PERCENTAGE 2012:")
print(Romney12prediction)

Obama12prediction = 100-Romney12prediction
print("OBAMA VOTE PERCENTAGE 2012:")
print(Obama12prediction)

#Trump Data 2016

indivProTrump16 = 132232784

pacProTrump16 = 	66141713

TrumpAssets16 = 333127164

#Clinton Data 2016

indivProClinton16 = 399670200

pacProClinton16 = 1785190

ClintonAssets16 = 1450335

#2016 Math

Trump16indiv = abs(indivProTrump16 - indivProClinton16)
while Trump16indiv > 100:
    Trump16indiv = Trump16indiv/4

Trump16pac = abs(pacProTrump16 - pacProClinton16)
while Trump16pac > 100:
    Trump16pac = Trump16pac/4
    
Trump16asset = abs(TrumpAssets16 - ClintonAssets16)
while Trump16asset > 100:
    Trump16asset = Trump16asset/4

Trump16prediction = (Trump16asset + Trump16pac + Trump16indiv)/3
print("TRUMP VOTE PERCENTAGE 2016:")
print(Trump16prediction)

Clinton16prediction = 100-Trump16prediction
print("CLINTON VOTE PERCENTAGE 2016:")
print(Clinton16prediction)