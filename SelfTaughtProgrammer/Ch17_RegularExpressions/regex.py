import re

# For metacharacter guidance
# https://www.w3schools.com/python/python_regex.asp

# open file text as a variable to use
with open("zen.txt", "r") as f:
    text = f.read()

# match explicit expression used many times
print(re.findall("Beautiful", text))

# ignore case in search
print(re.findall("beautiful",text,re.IGNORECASE))

# Using the wild card
pattern = "is......to explain"
print(re.findall(pattern,text,re.IGNORECASE))

# extracting a social security number
pattern = r"\d{3}-\d{2}-\d{3}"
print(re.findall(pattern,text,re.IGNORECASE))

# extracting a phone number
pattern = r"[(]?\d{3}[)]?\s?[-]?\d{3}-\d{4}"
print(re.findall(pattern,text,re.IGNORECASE))

# extracting a date
pattern = r"\d{1,2}/\d{1,2}/\d{4}"
print(re.findall(pattern,text,re.IGNORECASE))

# extracting phrases
pattern = r"it[a-zA-Z ']*idea."
print(re.findall(pattern,text,re.IGNORECASE))

# extracting email addresses - simple
regex = r'[\w\.\-]+\@.+\..{2,3}'
print(re.findall(regex,text))

# extracting email addresses - more complex
regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
print(re.findall(regex,text))

# see https://www.wired.com/2008/08/four-regular-expressions-to-check-email-addresses/
