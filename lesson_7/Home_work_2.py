def correct_sentence(sentence1, sentence2):
    corrected_sentence1 = sentence1.capitalize()[:-1] + '.' if sentence1[-1] in ['.', '!', '?'] else sentence1.capitalize() + '.'
    corrected_sentence2 = sentence2.capitalize()[:-1] + '.' if sentence2[-1] in ['.', '!', '?'] else sentence2.capitalize() + '.'
    return corrected_sentence1, corrected_sentence2

sentence1 = "hello world!"
sentence2 = "i love python"
corrected_sentence1, corrected_sentence2 = correct_sentence(sentence1, sentence2)
print(corrected_sentence1)
print(corrected_sentence2)