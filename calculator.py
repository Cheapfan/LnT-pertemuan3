def plus(a,b):
    return a+b
def min(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

a = float(input("Enter a number : "))
while True:
    operation = (input("Enter your operation : "))
    if operation == "=":
        break
    b = float(input("Enter a number : "))
    if operation == "+":
        print(a," + ",b," = ",plus(a,b))
        a = plus(a,b)
    elif operation =="-":
        print(a," - ",b," = ",min(a,b))
        a = min(a,b)
    elif operation =="*":
        print(a," * ",b," = ",multiply(a,b))
        a = multiply(a,b)
    elif operation =="/":
        print(a," / ",b," = ",divide(a,b))
        a = divide(a,b)
    else:
        print("error please re-input the operation and the second number")

print("The number you get = ",a)
