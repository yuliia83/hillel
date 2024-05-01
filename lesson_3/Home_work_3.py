import math

lst = [0, 1, 2, 3, 4, 5, 6]
length = len(lst)
mid = math.ceil(length / 2)
left = lst[0:mid]
right = lst[mid:length]
result = [left, right]
print(result)
