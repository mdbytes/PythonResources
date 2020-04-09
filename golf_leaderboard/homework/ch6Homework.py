#  Martin Dwyer
#  Introduction to Programming Logic
#  Kirkwood Community College, Spring 2017

#  Chapter Six: Homework
#  Submitted April 26, 2017

#  Notes on Assignment
#  Four friends want to determine who won their game of golf. Each has saved 
#  their score for 18 holes for a file with their name, such as Bob.txt, 
#  Colette.txt, etc. Your task is to write a program that:

    #  Prompts for the names of the 4 friends
    #  Prompts for how many holes of golf were played. (typically 9 or 18)
    #  Opens each friends file and calculates the score. 
    #  Outputs to a file named outcome.txt, the score for each friend and 
    #  Identify who was the winner like.

#  Files provided for use with this program:
    
    #  martin.txt consisting of 18 numeric scores for a round of golf
    #  bob.txt consisting of 18 numeric scores of a round of golf
    #  lucy.txt consisting of 18 numeric scores of a round of golf
    #  jane.txt consisting of 18 numeric scores of a round of golf
    #  waldo.txt consisting of 17 numeric scores and one string 'wd'
    
#  The program below tabulates and displays the golfing results 

def main():
                
    # Welcome the user
    print('')
    print('This program collects four golfers scorecards, calculates totals')
    print('and prints final standings for the foursome.')
    print('')

    # Prompt for names, get files, add scores, save individual names along with
    # holes played, and scores for the day in a file (scores.txt)    
    scoreTotals()
    
    # Algorithm to establish ranking of the four scores including output 
    # with ranking to leaderboard.txt
    scoreRanking()

    # Establish winner, 2nd, 3rd, and 4th place, printing the scores in 
    # order of their rank, name, holes played, score, and prize position    
    outputFinalStandings()
    
    
def scoreTotals():
    
    # Open file for tabulated game scores to be written
    scoreTotals = open('scores.txt','w')
    
    # Get file, tabulate score, and write to scores.txt for each player
    for players in range(0,4):

        # Initialize the game score variable and establish a Boolean variable
        # to indicate whether or not we have finished processing each player.
        gameScore = 0
        fileName = False
    
        while fileName == False:
        
            # Attempt to get a proper filename from the user
            try:
                firstName = input('Players First Name: ')
                print('')
                holesPlayed = int(input('Number of holes played:  '))
                print('')
                scoreCard = firstName + '.txt'
                scoresFile = open(scoreCard,'r')
    
            # If filename not valid, advise user to verify file and try again
            except FileNotFoundError: 
                print('')
                print('There was a problem finding',scoreCard)
                print('Please verify the filename and try again!')
                print('')
        
            # If filename is valid, tabulate and write to scores.txt    
            else:
                fileName = True

                #  Add up the scores in the player's .txt file for game score
                try:
                    for holes in range(1,holesPlayed+1):
                        gameScore += int(scoresFile.readline())
                
                # If  numeric scores lacking or errant, player's score is 999
                except ValueError:
                    print('Unrecognized value found in scorecard,',scoreCard)
                    print('A game score of 999 has been assigned to',firstName)
                    print('')
                    gameScore = 999
                
                # Write player's data to scores.txt
                scoreTotals.write(firstName+'\n')
                scoreTotals.write(str(holesPlayed)+'\n')
                scoreTotals.write(str(gameScore)+'\n')
    
    scoresFile.close()

def scoreRanking():
    
    lowScore = 999
    secondBest = 999
    thirdBest = 999
    highScore = 0
    secondDiff = 999
    thirdDiff = 999
    
    #  Determine high score and low score
    scoreTotals = open('scores.txt','r')
    for line in range(0,4):
        name = scoreTotals.readline()
        holesPlayed = int(scoreTotals.readline())
        gameScore = int(scoreTotals.readline())
        if gameScore <= lowScore:
            lowScore = gameScore
        if gameScore >= highScore:
            highScore = gameScore
    scoreTotals.close()
            
    # Determine Second Best Score (variable secondBest)
    scoreTotals = open('scores.txt','r')
    for line in range(0,4):
        name = scoreTotals.readline()
        holesPlayed = int(scoreTotals.readline())
        gameScore = int(scoreTotals.readline())
        if (gameScore-lowScore) < secondDiff and (gameScore-lowScore) > 0:
            secondBest = gameScore
            secondDiff = gameScore - lowScore
    scoreTotals.close()
            
    # Determine Third Best Score (Closest to First Place)
    scoreTotals = open('scores.txt','r')
    for line in range(0,4):
        name = scoreTotals.readline()
        holesPlayed = int(scoreTotals.readline())
        gameScore = int(scoreTotals.readline())
        if (highScore-gameScore) < thirdDiff and (highScore-gameScore) > 0:
            thirdBest = gameScore
            thirdDiff = highScore - gameScore
    scoreTotals.close()
    
    # Assign each player their position and write results to leaderboard.txt
    scoreTotals = open('scores.txt','r')
    leaderBoard = open('leaderboard.txt','w')
    for line in range(0,4):
        name = scoreTotals.readline()
        holesPlayed = int(scoreTotals.readline())
        gameScore = int(scoreTotals.readline())
        if gameScore == lowScore:
            position = 1
        if gameScore == highScore:
            position = 4
        if gameScore == secondBest:
            position = 2
        if gameScore == thirdBest:
            position = 3
        leaderBoard.write(name)
        leaderBoard.write(str(holesPlayed)+'\n')
        leaderBoard.write(str(gameScore)+'\n')
        leaderBoard.write(str(position)+'\n')
    scoreTotals.close()
    leaderBoard.close()

    # Print game summary.  This was a key validation point in programming.
    print('')
    print('GOLF GAME HIGHLIGHTS:')
    print('')
    print('The lowest score: ',lowScore)
    print('The highest score: ',highScore)
    
def outputFinalStandings():

    # This algorithm uese leadership.txt to take each player's data, print
    # them in order, and output the data to outcome.txt as assignment requires
    leaderBoard = open('leaderboard.txt','r')
    finalStanding = open('outcome.txt','w')
    finalStanding.write('Rank\t')
    finalStanding.write('Name\t')
    finalStanding.write('Holes\t')
    finalStanding.write('Score\t')
    finalStanding.write('Prize\n')
    
    # Output data for winner
    for line in range(0,4):
        name = leaderBoard.readline()
        name = name.rstrip('\n')
        holesPlayed = int(leaderBoard.readline())
        gameScore = int(leaderBoard.readline())
        position = int(leaderBoard.readline())
        if position == 1:
            prize = 'WINNER'
            finalStanding.write(str(position)+'\t')
            finalStanding.write(name+'\t')
            finalStanding.write(str(holesPlayed)+'\t')
            finalStanding.write(str(gameScore)+'\t')
            finalStanding.write(prize+'\n')
    leaderBoard.close()
    finalStanding.close()

    # Output data for 2nd place golfer
    leaderBoard = open('leaderboard.txt','r')
    finalStanding = open('outcome.txt','a')
    for line in range(0,4):
        name = leaderBoard.readline()
        name = name.rstrip('\n')
        holesPlayed = int(leaderBoard.readline())
        gameScore = int(leaderBoard.readline())
        position = int(leaderBoard.readline())
        if position == 2:
            prize = '2nd Place'
            finalStanding.write(str(position)+'\t')
            finalStanding.write(name+'\t')
            finalStanding.write(str(holesPlayed)+'\t')
            finalStanding.write(str(gameScore)+'\t')
            finalStanding.write(prize+'\n')
    leaderBoard.close()
    finalStanding.close()

    # Output data for 3rd place golfer
    leaderBoard = open('leaderboard.txt','r')
    finalStanding = open('outcome.txt','a')
    for line in range(0,4):
        name = leaderBoard.readline()
        name = name.rstrip('\n')
        holesPlayed = int(leaderBoard.readline())
        gameScore = int(leaderBoard.readline())
        position = int(leaderBoard.readline())
        if position == 3:
            prize = '3rd Place'
            finalStanding.write(str(position)+'\t')
            finalStanding.write(name+'\t')
            finalStanding.write(str(holesPlayed)+'\t')
            finalStanding.write(str(gameScore)+'\t')
            finalStanding.write(prize+'\n')
    leaderBoard.close()
    finalStanding.close()

    # Output data for 4th place golfer
    leaderBoard = open('leaderboard.txt','r')
    finalStanding = open('outcome.txt','a')         
    for line in range(0,4):
        name = leaderBoard.readline()
        name = name.rstrip('\n')
        holesPlayed = int(leaderBoard.readline())
        gameScore = int(leaderBoard.readline())
        position = int(leaderBoard.readline())
        if position == 4:
            prize = '4th Place'
            finalStanding.write(str(position)+'\t')
            finalStanding.write(name+'\t')
            finalStanding.write(str(holesPlayed)+'\t')
            finalStanding.write(str(gameScore)+'\t')
            finalStanding.write(prize+'\n')
    leaderBoard.close()
    finalStanding.close()

    # Print final standings to the screen, identifying outcome.txt
    print('')
    print('')
    print('FINAL STANDINGS FOR GOLF ROUND:')
    print('')
    finalStanding = open('outcome.txt','r')   
    for line in range(0,5):
        print(finalStanding.readline())
    print('These standings have been saved to outcome.txt')
    finalStanding.close()
    
     
main()        
        
    



       
