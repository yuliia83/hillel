def sekond_index (string, target):
    first_index = string.find (target)
    if first_index == -1:
        return None
    second_index = string.find(target, first_index + 1)
    if second_index == -1:
        return None
    return second_index


print(sekond_index("var", "a"))