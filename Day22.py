import json
student={
    "name":"vamsi",
    "age":21,
    "branch":"CSM"
}
data=json.dumps(student)
print(data)
print(type(data))

english='{"name":"vamsi","age":21}'
eng=json.loads(english)
print(eng)
print(type(eng))

store={
    "name":"laptop",
    "price":50000,
    "brand":"lenove"
}
sto=json.dump(store)

with open("student.json","r") as file:
    student=json.load(file)
    print(student)

tel={
    "name":"vamsi",
    "age":21
}

telu=json.dumps(tel)
print(telu)
print(type(telu))

telugu=json.load(tel)

with open("employee.json", "r") as file:
    employee=json.load(file)
    print(employee["employeename"])
    print(employee["department"])
    print(employee["skills"])




