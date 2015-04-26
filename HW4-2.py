import numpy as np
import matplotlib.pyplot as mplt

x = np.linspace(0,6,10000)
y = np.sin(x)
n = np.random.normal(0,0.1,10000)
z = y+n

mplt.subplot(2,1,1)
mplt.plot(x,z,'b-')
mplt.plot(x,y,'w--')
mplt.xlabel('Radians')
mplt.ylabel('Values')
mplt.title('Sine wave in noise [0:6]')
mplt.legend(['Signal+Noise','Signal'])
mplt.show(block=False)

mplt.subplot(2,2,3)
mplt.plot(x,z,'b-')
mplt.plot(x,y,'w--')
mplt.axis([1,1.5,0.5,1.5])
mplt.xlabel('Radians')
mplt.ylabel('Values')
mplt.title('Sine wave in noise [1:1.5]')
mplt.legend(['Signal+Noise','Signal'])
mplt.show(block=False)

mplt.subplot(2,2,4)
mplt.plot(x,z,'b-')
mplt.plot(x,y,'r--')
mplt.axis([1,1.05,0.5,1.5])
mplt.xlabel('Radians')
mplt.ylabel('Values')
mplt.title('Sine wave in noise [1:1.05]')
mplt.legend(['Signal+Noise','Signal'])
mplt.show(block=False)
