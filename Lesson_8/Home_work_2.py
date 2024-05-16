def is_palindrome(s):
    cleaned_string = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("0P") == False
    assert is_palindrome("a.") == True
    assert is_palindrome("aurora") == False

    print(is_palindrome(("A man, a plan, a canal: Panama")))
    print(is_palindrome("r."))
    print(is_palindrome("life is good"))


