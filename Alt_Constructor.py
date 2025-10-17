# Here we will write an example code for alternative constructor
# So let's say you get some input in a different format than the others, in this case alternate constructor comes in use
# It uses class method as it belongs to class instead of any instance of the class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromStr(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

p1 = Person("Sam", 24)
print(p1.name)
print(p1.age)

p2 = Person.fromStr("Alberto Del Rio, 27")
print(p2.name)
print(p2.age)