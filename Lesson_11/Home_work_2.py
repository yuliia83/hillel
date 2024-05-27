from inspect import isgenerator
def generate_cube_numbers(limit):
    num = 2
    while True:
        cube = num ** 3
        if cube >= limit:
            return
        yield cube
        num += 1

if __name__ == "__main__":


    gen = generate_cube_numbers(1)
    assert isgenerator(gen) == True
    assert list(generate_cube_numbers(10)) == [8]
    assert list(generate_cube_numbers(100)) == [8, 27, 64]
    assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729]

for cube in generate_cube_numbers(100):
    print(cube)