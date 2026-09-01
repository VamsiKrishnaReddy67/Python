import os
locations=os.getcwd()
print(locations)

files=os.listdir()
print(files)

print(os.path.exists("Day2.py"))

# os.mkdir("practice")

print(os.path.isdir("practice"))

path=os.path.join("project","data","student.txt")
print(path)

given="E:\\python project\\Student.json"
print(os.path.basename(given))

print(os.path.dirname(path))

# os.mkdir("os_practice.py")
pat=os.getcwd()
print(pat)
list=os.listdir()
print(list)
print(os.path.exists("Day25.py"))
print(os.path.isdir("Day25.py"))
create=os.path.join("Day25","Student.txt")
print(create)
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.dirname(path))


