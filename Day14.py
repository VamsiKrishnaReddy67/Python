student={
    "name": "vamsi",
    "age": 21,
    "branch": "CSM"
}
print(student["name"])
print(student["age"])

product={
    "name": "laptop",
    "price": 50000,
}
product["brand"]="LENOVO"
print(product)

employee={
    "name": "rahul",
    "salary": 50000
}
employee["salary"]=35000
print(employee)

user={
    "username": "vamsi",
    "email": "vamsi@example.com"
}
print(user.keys())
print(user.values())
print(user.items())

car={
    "brand": "toyota",
    "model": "Innova",
    "year": 2024
    }
car.pop("year")
print(car)

students={
    "name": "vamsi",
    "age": 21,
    "branch": "CSM"
}
students["city"]="markapur"
students.update({"age": 22})
print(students.keys())
print(students.values())
students.pop("branch")
print(students)
