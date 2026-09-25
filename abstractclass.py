from abc import ABC,abstractmethod
class shape(ABC):
    def area(self):
        pass
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return (self.l+self.w)*2
#object creation
ob1=rectangle(4,5)
print(ob1.area())
print (ob1.perimeter())