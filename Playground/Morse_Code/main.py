
def main():
    string = get_string()
    code = morse_encode(string)
    display(code)

def get_string():
    return input("Enter a string to be converted to Morse code: ")

def morse_encode(string):
    morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', ' ': ' '}
    encrypted=""
    for c in string:
        try: 
            encrypted += morse_code[c.upper()]
        except KeyError: 
            encrypted += ""
    
    return encrypted

def display(code):
    print(code)

main()

