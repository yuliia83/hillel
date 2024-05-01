lst = [1, 3, 5, 7, 2]

even_sum = 0
for i in range(0, len(lst), 2):
    even_sum += lst[i]
if not lst:
    result = 0
else:
    even_sum = sum(lst[:-1])
    last_element = lst[-1]
    result = even_sum * last_element
print(result)

