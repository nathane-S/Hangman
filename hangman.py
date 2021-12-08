class Game:
    def _init_(self, word):
        self.word = word
        self.state = "initializing"
        self.attempts = 3

    def guess(self, letter):

        if letter not in self.word:
            self.state = "wrong_guess"
            self.attempts = self.attempts - 1
            if self.attempts == 0:
                self.state = "lose_game"

        if letter in self.word:
            self.state = "right_guess"