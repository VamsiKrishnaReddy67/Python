file=open("hello.txt","w")
file.write("hello python")
file.close()

file=open("hello.txt","r")
print(file.read())
file.close()

file=open("hello.txt","a")
file.write("\nwelcome to full stack development")
file.close()

file=open("hello.txt","r")
print(file.read())
file.close()

file=open("student.txt","w")
file.write("Name:vamsi\nAge:21\nBranch:CSM")
file.close()

with open("student.txt","r") as file:
    print(file.read())

file=open("employee.txt","w")
file.write("Name:Rahul\nsalary:30000\nDepartment:IT")
file.close()
file=open("employee.txt","a")
file.write("\ncity:Hyderabad")
file.close()
with open("employee.txt","r") as file:
    print(file.read())