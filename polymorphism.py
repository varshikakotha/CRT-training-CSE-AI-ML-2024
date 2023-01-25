#when there are two functions with same name and different signature -- method overloading
#the latest updated method is taken
#same method name and same signature used in two differnt classes -- method overridiing
class Animal:
    def cat(self):
        print("cat says meow1")
    def dog(self):
        print("dog barks1")
    def cow(self):
        print("cow says aa1")
class Cat(Animal):
    def cat(self):
        print("cat says meow2")
    def eats(self):
        print("yes")
class Dog(Animal):
    def dog(self):
        print("dog barks2")
    def eats(self):
        print("yes")
class Cow(Animal):
    def cow(self):
        print("cow says aa2")
obj = Dog()
obj.dog()

