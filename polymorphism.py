class dog:
    def bark(self):
        return "bhoo!"
    
class cat:
    def bark(self):
        return "meww!"
    
#creating object
animals=[dog(),cat()]
for animal in animals:
    print(animal.bark())