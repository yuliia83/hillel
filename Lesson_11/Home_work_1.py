from inspect import isgenerator
def prime_generator(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    for num in range(2, n + 1):
        if is_prime(num):
            yield num

if __name__ == "__main__":
    gen = prime_generator(10)
    assert isgenerator(gen) == True
    assert list(prime_generator(10)) == [2, 3, 5, 7]
    assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
    assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(list(prime_generator(10)))  # Output: [2, 3, 5, 7]
