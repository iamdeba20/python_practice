import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,6.3,500)
y1=np.sin(x)
y2=np.sin(3*x)/3
y3=np.sin(5*x)/5
y4=np.sin(7*x)/7
y_sum=y1+y2+y3+y4
fig,ax=plt.subplots()
ax.plot(x,y1,label="y=sin(x)",ls="-")
ax.plot(x,y2,label="y=sin(3x)/3",ls="--")
ax.plot(x,y3,label="y=sin(5x)/5",ls=":")
ax.plot(x,y4,label="y=sin(7x)/7")
ax.plot(x,y_sum,label="y_sum=y1+y2+y3+y4",ls="-.")
ax.legend()
plt.show()