'''First we define the GOS_Erlang function which uses Erlang B formula to calculate Grade of service'''
'''The function GOS_Erlang takes no of Channels(C) and capacity in Erlangs (A) and return Grade of Service'''

import math

def GOS_Erlang(C,A):
    num = (A**float(C))/float(math.factorial(C))
    sum =0
    for k in range(C+1):
        sum+= (A**k)/float(math.factorial(k))
    GOS = num/sum
    return GOS

'''E_Erlang function computes the capacity in Erlang for a given Grade of Service and number of channel.
The function uses the GOS_Erlang and perform a binary search for the capacity '''

def E_Erlang(GOS,channel):
    a_test= float(0)
    b_test = float(channel)
    c_test= (a_test+b_test)/2
    GOS_a = GOS_Erlang(channel,a_test)
    GOS_b = GOS_Erlang(channel,b_test)
    GOS_c = GOS_Erlang(channel,c_test)
    while(math.fabs(GOS-GOS_c) >.000001):
        if(GOS_c<GOS):
            a_test=c_test
        else:
            b_test=c_test
        c_test= (a_test+b_test)/2
        GOS_c = GOS_Erlang(channel,c_test)
    return c_test

''' The main function is defined which has all the assigned Channels and prints the eastimated Capacity'''

def main():
    channels=[7,15,22,30,37,45,52,60]
    GOS=0.01
    print("GOS of 0.01")
    for channel in channels:
        print("Channel {0:d}    Capacity {1:.3f}".format(channel,E_Erlang(GOS,channel)))

if __name__ == "__main__":
    main()    
