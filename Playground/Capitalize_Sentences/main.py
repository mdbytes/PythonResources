def main():
    paragraph = get_paragraph()
    capitalized = capitalize_paragraph(paragraph)
    display(capitalized)

def get_paragraph():
    return input("Enter a paragraph here: ") 

def capitalize_paragraph(paragraph):
    
    sentence_starts_at = 0
    ends_with = ["?","!","."]
    sentences = []

    for k in range(0,len(paragraph)):
        if paragraph[k] in ends_with:
            sentences.append(paragraph[sentence_starts_at:k+1].lstrip())
            sentence_starts_at = k+1
        k+= 1

    capitalized = ""

    for sentence in sentences: 
        capitalized += sentence[0].upper() + sentence[1:] + " "

    return capitalized

def display(capitalized):
    print(capitalized)

main()


# For testing: 
# "This is a paragraph.  it contains words that should be capitalized.  this is good, right?  right!"