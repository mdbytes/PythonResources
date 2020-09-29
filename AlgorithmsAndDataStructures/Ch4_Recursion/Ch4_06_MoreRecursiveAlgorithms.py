"""
Continued solutions to select problems from MyProgrammingLab problems - Getting started with Python
"""

"""
Write a recursive function, len, that accepts a parameter that holds a string value, and returns the number of characters in the string.
The length of the string is:
0 if the string is empy ("")
1 more than the length of the string beyond the first character
"""


def len(aString):
    if aString == "":
        return 0
    else:
        return 1 + len(aString[1:])


"""
Write a recursive function, containsVowel, which accepts one parameter containing a string value and returns True if the string contains a vowel.

A string contains a vowel if:
The first character of the string is a vowel or
The rest of the string (beyond the first character) contains a vowel
"""


def containsVowel(aString):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if len(aString) == 0:
        return False
    elif aString[0] in vowels:
        return True
    elif len(aString) > 0:
        return containsVowel(aString[1:])


"""
Write a recursive function, replace, that accepts a parameter containing a string value and returns another string value, the same as the original string except with each blank replaced by an asterisk "*".

Replacing the blanks in a string involves:
Nothing if the string is empty
Otherwise
If the first character is not a blank, simply concatenate it with the result of replacing the rest of the string.
If the first character IS a blank, concatenate an asterisk with the result of replacing the rest of the string.

"""


def replace(aString):
    tempString = ""
    if aString == "":
        return aString
    if aString[0] == " ":
        tempString += "*" + replace(aString[1:])
    else:
        tempString += aString[0] + replace(aString[1:])

    return tempString


"""
Write a recursive function, reverse, that accepts a parameter containing a string value and returns the original string in reverse. For example, calling reverse('goodbye') would return 'eybdoog'.

Reversing a string involves:
No action if the string is empty or only has 1 character
Concatenating the last character with the result of reversing the string consisting of the second through next-to-last character, followed by the first character

"""


def reverse(aString):
    if len(aString) <= 1:
        return aString
    else:
        return aString[-1] + reverse(aString[:-1])


"""
A palindrome is a word or phrase that reads the same forwards or backwards (e.g. "dad", "mom", "deed").
Write a recrusive function, isPalindrome that accepts a string and returns whether the string is a palindrome. A string is a palindrome if:
it is an empty string or consists of a single letter, or
if the first and last characters are the same, and the rest of the string forms a palindrome
Your function should ignore spaces and only compare letters.
"""


def isPalindrome(aString):
    aString = aString.replace(" ", "")
    if len(aString) <= 1:
        return True
    if aString[0] == aString[-1]:
        return isPalindrome(aString[1:-1])
    else:
        return False


print(isPalindrome("toot"))
print(isPalindrome("pickles"))
print(isPalindrome("never odd or even"))

"""
The elements of a tuple can be set to 0 recursively as follows:
If the tuple has a length of zero, nothing should be done to it.
Otherwise, set the first element of the tuple to 0, and then append it to the rest of the tuple.
Write a function named clearthat accepts one argument, a tuple of any length, and returns a tuple of the same length with every element set to 0.

"""


def clear(tup):
    if not tup:
        return ()
    return (0,) + clear(tup[1:])

