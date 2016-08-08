from secret import SecretWord
from board import Board

class Game:
    """Run an entire game.

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess correct letters
       - returns final board
    winner returns the player who picked the last letter.

    >>> from wordset import Dictionary
    >>> from player import Player, DummyPlayer
    >>> p = Player(Dictionary("assets/lincoln.txt"))
    >>> game = Game(DummyPlayer("pick"), [ DummyPlayer("guess") ] )
    >>> board = game.play(False)
    >>> board.word()
    ['s', 'c', 'o', 'r', 'e']
    >>> len(board.guesses())
    6
    """
    def __init__(self, picker, guessers):
        # BEGIN
        self.picker = picker
        self.guessers = guessers
        self.winner = guessers
        # END

    def play(self, verbose=True):
        # BEGIN
        pickers_word = self.picker.pick_word()
        secret = SecretWord(pickers_word)
        board = Board(secret)
        while board.done() == False:
            for guesser in self.guessers:
                if verbose:
                    board.display()
                self.winner = guesser
                attempt = guesser.guess(board)
                board.guess(attempt)
                while len(secret.match(attempt)) > 0 and board.done() == False:
                    attempt = guesser.guess(board)
                    board.guess(attempt)
        return board
        # END

    def winner(self):
        # BEGIN
        return self.winner
        # END
