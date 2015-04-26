import numpy as np
import matplotlib.pyplot as plt

random1 = np.random.normal(0,1/np.sqrt(2),100000)
random2 = np.random.normal(0,1/np.sqrt(2),100000)
complex_number= random1 + 1j*random2
abs_value = np.abs(complex_number)
plt.hist(abs_value,100,facecolor='g')
plt.grid(True)
plt.xlabel('Distribution Value')
plt.ylabel('Number of occurrences')
plt.title('Rayleigh distribution histogram, 100000 Samples')
plt.show()
