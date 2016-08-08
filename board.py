"""Board class for hangman game."""

class Board:
    """Board for hangman with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        self.board = ['_'] * len(secret)
        self.guessed = []
        self._secret = secret
        # END

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        return len(self.board)
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        self.guessed += char
        char_positions = self._secret.match(char)
        for pos in char_positions:
            self.board[pos] = char
        return len(char_positions)

    def word(self):
        """Return the current state of guessing the word as a list of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        return self.board
        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        return self.guessed
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        correct_chars = [correct for correct in self.board if correct != '_']
        return list(set(correct_chars))
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        return [wrong for wrong in self.guesses() if wrong not in self.board]
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        if '_' not in self.board:
            return True
        elif len(self.misses()) == Board.max_miss:
            return True
        else:
            return False
        # END

    max_miss = 11
    def miss_man(missed):
        missed = min(missed, Board.max_miss)
        return "assets/man{0}.txt".format(missed)

    def display(self):
        missed = len(self.misses())
        path = Board.miss_man(missed)
        with open(path) as fp:
            symbol = fp.read()
        print(symbol)
        print(self.word())
        print("Guessed chars: ", self.guesses())
