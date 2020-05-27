"""
An anagram is a word created by rearranging letters of another word.
Write an algorithm that determines if a word is an anagram of another.
"""


def is_anagram(word_one: str, word_two: str) -> bool:
    return sorted(word_one.lower()) == sorted(word_two.lower())


def app():
    print(is_anagram("iceman","cinema"))
    print(is_anagram("this","that"))


if __name__ == '__main__':
    app()
