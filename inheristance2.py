class a:
    def show(self):
        print("a is show")
class b(a):
    def show(self):
        print("b is show")
        super().show()
class c(b):
    def show(self):
        print("c is show")
class d (c,b):
    def show(self):
        print("d is show")
        super().show()
#creating object
ob=d()
ob.show()