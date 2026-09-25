from dataclasses import dataclass
@dataclass
class student:
    name:str
    age:int
s=student("john",18)
print(s)