class animal:
    def bark(self):
        print("every animal barks")

class dog (animal):
    def walk(self):
        
        print("dog walk in four legs")

d=dog()
print(d.bark())
print(d.walk())