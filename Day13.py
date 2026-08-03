numbers={10,20,30,20,10}
print(numbers)

fruits={"apple","banana"}
fruits.add("mango")
print(fruits)

colors={"red","blue","green"}
colors.remove("blue")
print(colors)

a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

skills={"python","HTML","CSS","JavaScript"}
print(skills)

frontend={"HTML","CSS","JavaScript"}
backend={"python","Django","JavaScript"}
print(frontend.union(backend))
print(frontend.intersection(backend))
print(frontend.difference(backend))
frontend.add("React")
frontend.remove("CSS")
print(frontend)
