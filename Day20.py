try:
    print(10/0)
except:
    print("Division by zero is not possible")


try:
    number=int(input("Enter a number:"))
    print(number)
except ValueError:
    print("Invalid input")

try:
    print(20/5)
except:
    print("Division by zero is not possible")
else:
    print("Division is successful")

try:
    print(10/10)
except:
    print("Division by zero is not possible")
finally:
    print("Program finished")

try:
    with open("sample.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

try:
    num=int(input("Enter a number:"))
    mem=int(input("Enter a number:"))
    print(num/mem)
except ZeroDivisionError:
    print("Division by zero is not possible")
finally:
    print("thank you ")

    
