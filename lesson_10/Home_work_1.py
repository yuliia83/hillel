def sequence_generator(func, first_member, n):

    current_member = first_member
    for _ in range(n):
        yield current_member
        current_member = func(current_member)

if __name__ == "__main__":


    def progression_rule(x):
        return x + 2

    gen = sequence_generator(progression_rule, 1, 5)

    for member in gen:
        print(member)
