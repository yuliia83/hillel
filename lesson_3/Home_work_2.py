def addition(a, b):
    return a + b

def subtraction(a, b):
    if a == 0:
        return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division cannot be zero!"
    else:
        return a / b

print("Selest an operation:")
print("1. addition")
print("2. subtraction")
print("3. multiplikation")
print("4. division")

opera = input("Ваш вибір (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if opera == '1':
    print("Result:", addition(num1, num2))
elif opera == '2':
    print("Result:", subtraction(num1, num2))
elif opera == '3':
    print("Result:", multiplikation(num1, num2))
elif opera == '4':
    print("Result:", division(num1, num2))
else:
    print("Incorrect choice of operation")

