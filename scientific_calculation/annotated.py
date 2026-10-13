import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 15, 10)
y = x**2

fig, ax = plt.subplots()
fig.set_facecolor("yellow")
ax.set_facecolor("red")

ax.plot(x, y)
ax.set(xlabel="x",ylabel="y",title="quadratic graph")
#ax.set_xlabel("x")
#ax.set_ylabel("y")
#ax.set_title("quadratic plot")
ax1=fig.add_axes([0.2,0.1,0.3,0.3])
#fig.add_axes([l,b,w,h]) l= left boarder , and value range from 0 to 1

ax1.plot(x,x**3)
print(fig.get_figheight())
print(fig.get_figwidth())

plt.show()
