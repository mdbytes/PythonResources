
def main():
    input_scores()
    display_scores()


def input_scores():
    more_players = True
    write_scores = open('Golf_Scores/golf_scores.txt','w')

    while more_players:
        name = input("Golfer name:  ") + '\n'
        score = input("Score:  ") + '\n'
        answer = input("Enter y for more golfers or enter to exit :")

        write_scores.write(name)
        write_scores.write(score)

        if answer != 'y':
            more_players = False
        
    write_scores.close()


def display_scores():
    read_scores = open('Golf_Scores/golf_scores.txt','r')
    print("\n\nGolfer\t\tScore")

    line = read_scores.readline()
    
    while line != '':
        golfer = line.rstrip('\n')
        score = read_scores.readline().rstrip('\n')
        print(golfer,'\t\t',score)
        line = read_scores.readline()

    print("\n\n")
    read_scores.close()


main()


