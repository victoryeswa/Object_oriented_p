#inheritance
#make an upper level class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print(' I do not know what to say!')
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

class Dog(Pet):
    def speak(self):
        print('Bark')
class Fish(Pet):
    pass

p = Pet('Tim', 19)
p.show()
c = Cat('Bill', 34)
c.speak()
d = Dog('Jill', 25)
d.speak()
e = Fish('kate', 18)
e.speak()
e.show()

