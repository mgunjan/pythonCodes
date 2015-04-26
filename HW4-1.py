import numpy as np
import matplotlib.pyplot as mplt
import sys

while True:
    acceptedip= input('Please provide an exponent n(enter \'q\' to exit)\n')
    try:
        n= float(acceptedip)
        x = np.linspace(0,10,num=101)
        y1 = np.power(x,n)* np.exp(-x)
        y2 = x/(x**2+1)
        mplt.plot(x,y1,'b-')
        mplt.plot(x,y2,'r-.')
        mplt.title('$x/x^2+1$ vs $x^n e^x $')
        mplt.xlabel('x,n= {0}'.format(n))
        mplt.ylabel('f(x)')
        mplt.grid(True)
        print('Please Close Graph Display to move on to Next Iteration')
        mplt.show()
    except ValueError:
        if acceptedip == 'q':
            sys.exit()
        else :
            print('enter valid input')
                
