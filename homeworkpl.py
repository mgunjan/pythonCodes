
'''Program to calculate RSL using various propogation model for distance 1,2,3...,20km'''

import math

hte = 40.0 #height of the cellular Basestation
hre = 1.5 #height of mobile
eirp = 54.0 
freq = 800.0 # frequency in MHz 

for d in range(1,21):
    fsl= 32.45 + (20*math.log10(freq)) + (20*math.log10(d))
    fel= (40*math.log10(d*1000)) - (20*math.log10(hte)) - (20*math.log10(hre))
    ohm= 69.55 + (26.16*math.log10(freq)) -(13.82*math.log10(hte))+ ((44.9-(6.55*math.log10(hte)))*math.log10(d)) -((((1.1*math.log10(freq))-0.7)*hre)-((1.56*math.log10(freq)-0.8)))
    tom= 32.45 + (20*math.log10(freq)) + (20*math.log10(.001))+ (30*math.log10(1000*d))
    rsl1= eirp - fsl 
    rsl2= eirp - fel
    rsl3= eirp - ohm
    rsl4= eirp - tom
    print("RSL level at distance of {0:d} km using FSL is {1:.2f}".format(d,rsl1))
    print("RSL level at distance of {0:d} km using FEL is {1:.2f}".format(d,rsl2))
    print("RSL level at distance of {0:d} km using Okomura-Hata model is {1:.2f}".format(d,rsl3))
    print("RSL level at distance of {0:d} km using 3rd order model  is {1:.2f}".format(d,rsl4))
    

    
