def common_elements():

    multiples_of_3 = [x for x in range(0, 100) if x % 3 == 0]
    multiples_of_5 = [x for x in range(0, 100) if x % 5 == 0]

    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)

    common_elements_set = set_3.intersection(set_5)

    return common_elements_set


# Перевірка функції
common_elements_set = common_elements()
print("Intersection:", common_elements_set)