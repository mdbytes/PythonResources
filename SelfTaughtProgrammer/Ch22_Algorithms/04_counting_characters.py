from typing import Dict

"""
Write an algorithm that returns the number of times each character occurs in a string
"""


def count_characters(string: str) -> dict:
    char_dict = {}
    for c in string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    # sorting the dict
    result = {}

    # first get a list of he keys in char_dict
    keys = sorted(char_dict)

    # then insert sorted values in the result set
    for k in keys:
        result[k] = char_dict[k]

    return result


def app():
    string = "abcdefghijk"
    print(count_characters(string))

    string = "mississippi"
    print(count_characters(string))


if __name__ == '__main__':
    app()

