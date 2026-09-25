age=[1,3,5,9] #list-unordered,mutable
print(age[0])
age[1]=4
print(age)
age.append(6)
age.pop(3)
age.insert(0,10)
print(age)
print(len(age))
for num in age:
    print(num)
    #tuples-ordered,immutable
    mark=(1,2,3,5,8)
    print(mark)