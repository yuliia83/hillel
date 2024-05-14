def move_the_last_element_to_the_beginning(lst):
    if len(lst) <= 1:
        return lst

    last_element = lst.pop()

    lst.insert(0, last_element)

    return lst

my_list = [1, 2, 3, 4, 5, 6]
now_list = move_the_last_element_to_the_beginning(my_list)
print(my_list)
