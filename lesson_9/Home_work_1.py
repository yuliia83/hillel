def popular_words(text, words):
    text = text.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = text.count(word)
    return word_count

text = "When I was One I had just begun When I was Two I was nearly new"
words = ["i", "was", "one", "new", "mama"]
print(popular_words(text, words))