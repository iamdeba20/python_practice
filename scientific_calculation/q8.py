import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,1000,100)
y=np.sqrt(x)
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_xscale('log')
plt.show()