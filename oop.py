class Dog:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Hagrid", "American Bully")

print(my_dog.name)
print(my_dog.bread)
my_dog.bark()


#Encapsulation
class Car:
    def __init__(self, make, model):
        self.make = make
        self._model = model

    def get_model(self):
        return self._model
    
    def set_model(self, model):
        self._model = model

my_car = Car("Toyota", "Corolla")

print(my_car.make)
print(my_car.get_model())

my_car.set_model("Carmy")
print(my_car.get_model())


#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

dog = Dog("Hagrid")
cat = Cat("Whisker")

dog.speak()
cat.speak()


#Polymorphism
class Bird:
    def sound(self):
        print("Bird chirps")

class Dog:
    def sound(self):
        print("Dog barks")

def animal_sound(animal):
    animal.sound()

bird = Bird()
dog = Dog()

animal_sound(bird)
animal_sound(dog)


#__str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
person = Person("channa", 28)
print(person)


#Class vs Instance Variables
class Car:
    wheel = 4 #calss variavle

    def __init__(self, make, model):
        self.make = make #instance variable
        self.model = model

car1 = Car("Toyota", "corolla")
car2 = Car("Honda", "civic")

print(car1.wheel)
print(car2.wheel)

