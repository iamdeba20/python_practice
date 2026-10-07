import numpy as np
import matplotlib.pyplot as plt
x=[0,1,2,3,4,5]
y=[1,4,9,16,25,36]
fig ,ax =plt.subplots()
ax.plot(x,y)
ax.annotate(text="maximum",xy=(5,36))

plt.show()