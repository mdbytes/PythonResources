from Ch15_BringingItAllTogether.game_of_war.player import Player
from Ch15_BringingItAllTogether.game_of_war.deck import Deck

class Game:
    def __init__(self):
        name1 = input("player1 name ")
        name2 = input("player2 name ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        response = None
        while len(cards) >= 2:
            response = input('q to quit. Any other key to play.')
            if response == 'q':
                break
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()
            print("{} drew {} {} drew {}".format(self.player1.name, player1_card, self.player2.name, player2_card))
            if player1_card > player2_card:
                self.player1.wins += 1
                print("{} wins this round".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} wins this round".format(self.player2.name))
        print("The War is over.{} wins".format(self.winner(self.player1, self.player2)))

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "It was a tie!"


def app():
    game = Game()
    game.play_game()


if __name__ == "__main__":
    app()