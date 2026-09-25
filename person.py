class Person:
    def __init__(Self, name, age):
        Self.name = name
        Self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.") 
my_person = Person("Brian", 20)
my_person.introduce()       