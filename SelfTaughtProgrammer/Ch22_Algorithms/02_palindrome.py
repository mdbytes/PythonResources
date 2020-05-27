"""
A palindrome is a word spelled the same way forward and backward.  Write
an algorithm that checks to see if a word is a palindrome.
"""


def is_palindrome(word: str) -> bool:
    word = word.lower()
    return word[::-1] == word


def app():
    print(is_palindrome("Mom"))
    print(is_palindrome("Mother"))


if __name__ == '__main__':
    app()
