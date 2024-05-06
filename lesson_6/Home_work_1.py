import string

def characters_between_letters(input_str):
    start, end = input_str.split('-')
    all_letters = string.ascii_letters
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)
    return all_letters[start_index:end_index + 1]

input_str = input("Введіть дві літери через дефіс: ")
print(characters_between_letters(input_str))