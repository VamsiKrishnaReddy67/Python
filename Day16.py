def show_number(*args):
    print(args)
show_number(10, 20, 30, 40)

def total(*args):
    print(sum(args))
total(5,10,5)

def student(**data):
    print(data)
student(name="vamsi", age=21)

multiply=lambda a,b:a*b
print(multiply(5,10))

numbers=[1,2,3,4,5]
result=list(map(lambda x:x*3, numbers))
print(result)

number=[10,11,12,13,14,15]
results=list(filter(lambda x:x%2==1, number))
print(results)