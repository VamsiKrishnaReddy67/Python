class student:
    def __init__(self):
        print("Student Created Successfully")
s1 = student()

class student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s2 = student1("vamsi",21)
print(s2.name)
print(s2.age)

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
s3=car("BMW","X5")
print(s3.brand)
print(s3.model)

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
s4=employee("vamsi",25000)
s4.show()

class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def detail(self):
        print("Brand: ", self.brand)
        print("Price: ", self.price)
s5=laptop("HP",50000)
s5.detail()

class mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def details(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)
s6=mobile("Samsung","M31",15000)
s6.details()
