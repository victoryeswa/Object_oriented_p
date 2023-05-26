class Person:
    number_of_people = 0
    GRAVITY = -9.8


    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = Person('Tim')
print(Person.number_of_people)
p2 = Person('Jill')
print(Person.number_of_people())

# 2

class Math:

    @staticmethod  #--not changing(meaning)
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10 
    
    @staticmethod
    def pr():
        print('run')

Math.pr()
    
print(Math.add5(5))
