class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says 'Meow!'")

    def eat(self):
        print(f"{self.name} is eating cat food.")

    def drink(self):
        print(f"{self.name} is drinking water")
    
my_cat = Cat(name="Whiskers")

my_cat.meow()  

my_cat.eat()

my_cat.drink() 

my_cat.sleep()
