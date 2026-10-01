import numpy as np
a=[1,4,-2]
b=[4,7,2]
c=[2,3,6]
ans=np.matmul(a,b)
dot=np.dot(a,b)
#print(dot)
t=np.dot(c,np.cross(a,b))
print(t)
#print(ans)