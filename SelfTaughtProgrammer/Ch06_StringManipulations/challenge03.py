sentence = "aldous Huxley was born in 1894"

new_sentence: str = ""

for i in range(0,len(sentence)):
    if i==0:
        new_sentence += sentence[i].capitalize()
    else:
        new_sentence += sentence[i]

print(new_sentence)