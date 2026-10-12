import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,15,10)
y=x**2
fig ,ax =plt.subplots()
print(fig.set_facecolor("yellow"))
print(ax.set_facecolor("red"))
fig.set_figheight(10)
fig.set_figwidth(12)
ax.plot(x,y)
print(fig.get_figheight())
print(fig.get_figwidth())
#ax.annotate(text="maximum",xy=(5,36))

plt.show()