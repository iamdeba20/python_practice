class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"my name is {self.name},and my age is {self.age}")

s1=student("debaprasad",23)
print(s1.details())