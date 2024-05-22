def is_even(numbers):
    return numbers % 2 == 0

if __name__ == "__main__":
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True

print(is_even(4))
print(is_even(7))