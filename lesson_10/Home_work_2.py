def first_word(text: str) -> str:
    text = text.strip(" , . ")
    words = text.split()
    for word in words:
        cleaned_word = word.strip(" ,. ")
        if cleaned_word:
            return cleaned_word
        return " "


if __name__ == "__main__ ":
    assert first_word("Hello world") == "Hello"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("don't touch it") == "don't"
    assert first_word(".., and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"

print(first_word("Hello, world!"))
print(first_word("   Привіт, світ!"))
print(first_word("...одне_слово..."))
print(first_word("Don't stop me now"))
print(first_word(" , , . . Привіт!"))