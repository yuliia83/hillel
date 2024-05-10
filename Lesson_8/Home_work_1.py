def add_one(input_list):
    num = int(''.join(map(str, input_list)))
    num += 1
    result_list = [int(x) for x in str(num)]
    return result_list

input_list = [1, 2, 3, 4]
result = add_one(input_list)
print(result)