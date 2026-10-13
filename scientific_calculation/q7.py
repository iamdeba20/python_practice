import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,500)
y=np.sin(x)+0.2*np.random.randn(500)
fig=plt.figure()
ax1=fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(x,y,color='b')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('noisy sin wave')
#insert axes
ax2=fig.add_axes([0.55,0.55,0.3,0.3])
ax2.plot(x,y,'r-')
ax2.set_title('enlarged portion')
ax2.axis([2,4,-1.5,0.5])
plt.show()