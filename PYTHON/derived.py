class Animal:
    def make_sound(self):
        self.name=name
    def eat(self):
        print("Some generic animal sound.")
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
class Bird(Animal):
    def make_sound(self):
        print("Tweet!")
animal={Dog(),Cat(),Bird()}
for animal in animal:
    animal.make_sound()


