from __future__ import division

import numpy as np
#import scipy.stats as stats
import matplotlib.pyplot as plt

k=0.4
x=np.arange(0,15,0.1)
y=k*np.exp(-k*x)
plt.plot(x,y,'-')
plt.title('Exponencial: $k$ =%.2f' % k,fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('Densidad de probabilidad',fontsize=15)
plt.show()