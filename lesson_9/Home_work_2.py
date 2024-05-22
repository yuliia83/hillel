def difference(*args):
    if not args:
        return 0

    max_value = max(args)
    min_value = min(args)

    return round(max_value - min_value, 2)


if __name__ == "__main__":
    assert difference(1, 2, 3) == 2
    assert difference(5, -5) == 10
    assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
    assert difference() == 0

print(difference(1, 2, 3))
print(difference(-1, -2, -3))
print(difference(1.1, 2.2, 3.3, -4.4))
print(difference())
