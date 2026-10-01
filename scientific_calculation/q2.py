import numpy as np
f1=1,4,5
f2=2,4,5
f3=7,8,9
f1_m=np.sqrt(f1[0]**2 +f1[1]**2 +f1[2]**2)
angle_f1_x=np.arctan(f1[0]/f1_m)
print(angle_f1_x)