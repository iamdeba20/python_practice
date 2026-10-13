import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,200)
y=np.sin(x)
fig=plt.figure()
#main axes
ax1=fig.add_axes([0.1,0.1,0.9,0.9])
ax1.plot(x,y,color='r')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.set_title('complete sin wave')
#insert axes
ax2=fig.add_axes([0.23,0.32,0.3,0.3])
ax2.plot(x,y,'g-')
ax2.set_title('zoomed portion')
ax2.axis([2,4,-1,1])
plt.show()