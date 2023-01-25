class A:
    name = "varshika"
    age = 20

class B(A):
    age = 10
class C(B):
    Roll = 101
class D(C):
    bus = "Yes"

obj = D()
obj.name = "Kumari"
print(obj.age)
print(obj.name)
print(obj.Roll)
print(obj.bus)
#name is not present in B but as B is child of A it inherit properties of A
#obj checks for defined values in it"s class if not present then it goes to it's parent class
