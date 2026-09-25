def rotate(x,y,z):
    return(z,x,y)
a,b,c="dog",4,7
print(a,b,c,sep=" ")
for i in range(3):
    a,b,c=rotate(a,b,c)
    print(f"iteration{i+1}=",a,b,c)

        
       