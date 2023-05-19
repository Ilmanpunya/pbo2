# ilman nafis al-fariq
# R4
# 210511144

# contoh

class Matematika:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c


mat = Matematika()
B = mat.add(5, 3, 4)
print(B)

mut = Matematika()
C = mut.add(7, 3)
print(C)


# contohlain

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())


#contoh sound

class Animal:
    def make_sound(self):
        print("the animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("the dog barks")
    
class Cat(Animal):
    def make_sound(self):
        print("the cat meows")

class Chihuahua(Dog):
    def make_sound(self):
        print("the chihuahua yaps")

class Siamese(Cat):
    def make_sound(self):
        print("the siamese purrs")

def animal_sound(animal):
    animal.make_sound()

#instatiate objects of each class
animal = Animal()
dog = Dog()
cat = Cat()
chihuahua = Chihuahua()
siamese = Siamese()

#call the animal_sound function for each object
animal_sound(animal)
animal_sound(dog)
animal_sound(cat)
animal_sound(chihuahua)
animal_sound(siamese)

#contoh abstrac

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("starting car....")

class motorcycle(vehicle):
    def start(self):
        print("starting motorcycle...")

class bus(vehicle):
    def start(self):
        print("starting bus...")

vehicle = [car(), motorcycle(), bus()]

for vehicle in vehicle:
    vehicle.start()


#contoh duck typing 

class Kucing:
    def bersuara(self):
        print("meoww")

class Anjing:
    def bersuara(self):
        print("anjiiing")

def cetak_suara(objek):
    objek.bersuara()

kucing = Kucing()
anjing = Anjing()

cetak_suara(kucing)
cetak_suara(anjing)

