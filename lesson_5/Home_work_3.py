import string
def to_hashtag(sentence):
    words = sentence.split()
    cleaned_words = [word.strip(string.punctuation).capitalize() for word in words]
    hashtag = '#' + ''.join(cleaned_words)
    hashtag = hashtag[:140]
    return hashtag

user_input = input("text: ")
result = to_hashtag(user_input)
print("Hashtag:", result)
