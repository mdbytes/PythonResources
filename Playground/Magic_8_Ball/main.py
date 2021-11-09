import random

def main():
    play_the_game()

def play_the_game():
    keep_playing = True
    while keep_playing:
        question = get_question()
        answer = get_answer()
        display_result(question,answer)
        keep_playing = keep_going()

def get_question():
    question = input("Type a question here: ")
    return question

def get_answer():
    infile = open('Playground/Magic_8_Ball/8_Ball_Responses.txt','r')
    responses = []
    line = infile.readline()
    while line != "":
        responses.append(line.strip())
        line = infile.readline()
    infile.close()
    selection = get_answer_number()
    print(len(responses))
    return responses[selection]

def get_answer_number():
    return random.randint(0,19)

def display_result(question,answer):
    print("Your question: ",question)
    print("The Magic 8 Ball Answer: ",answer)

def keep_going():
    response = input("Enter 'y' for another question, 'n' to quit: ")
    if response == 'y':
        return True
    else:
        return False

main()