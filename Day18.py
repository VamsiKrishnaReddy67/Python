class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass 
c=Dog()
c.sound()

class cat:
    def sound(self):
        print("meows")
class dog(cat):
    def sound(self):
        print("Barks")
d=dog()
d.sound()

class cat1:
    def sound(self):
        print("meows")
class dog1(cat1):
    def sound(self):
        print("Barks")
c1=cat1()
d1=dog1()
c1.sound()
d1.sound()

class student:
    def __init__(self):
        self._marks=95
    def show(self):
        print("Marks: ", self._marks)
s=student()
s.show()

class laptop:
    def start(self):
        print("Laptop started")
m=laptop()
m.start()

class person:
    def show1(self):
        print("i am a  Person ")
class employee(person):
    def show1(self):
        print("i am an Employee")
e=employee()
e.show1()
