def multiply_digits(number):
    result = 1
    while number >= 10:
        digits = [int(digit) for digit in str(number)]
        product = 1
        for digit in digits:
            product *= digit
        result = product
        number = product
    return result

user_input = int(input("enter an integer: "))
result = multiply_digits(user_input)
print("Result:", result)