def find_unique_value(some_list):
   counts = {}
   for num in some_list:
       if num in counts:
           counts[num] += 1
       else:
           counts[num] = 1

   for num, count in counts.items():
       if count == 1:
           return num
   return None


if __name__ == "__main__":

    assert find_unique_value([1, 2, 1, 1]) == 2
    assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
    assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5



some_list = [1, 2, 5, 2, 1]
print(find_unique_value(some_list))