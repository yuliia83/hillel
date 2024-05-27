def is_even(n: int) -> bool:
    return (n & 1) == 0

if __name__ == "__main__":
    assert is_even(2494563894038 ** 2) == True
    assert is_even(1056897 ** 2) == False
    assert is_even(24945638940387 ** 3) == False

print(is_even(3))
print(is_even(6))