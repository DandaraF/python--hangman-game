from kick.kick import Kick
from message.message import Message
from gallows_drawing.gallows_drawing import Gallows
from secret_word.secret_word import SecretWord
import os


class Game:

    def __init__(self):
        self.max_error = 7
        self.error = 0
        self.message = Message()
        self.gallows = Gallows()
        self.get_secret_word = SecretWord()
        self.valid_kick = Kick()
        self.secret_word = ''
        self.kick = ''
        self.letter = []
        self.camouflage_word = []
        self.game_over = False

    def camouflage_secret_word(self, secret_word):
        return ['_' for line in secret_word]

    def add_letter_kick(self, kick):
        self.letter.append(kick)
        print('Letras chutadas = > ', self.letter)

    def add_letters_to_array(self):
        index = 0

        for letter in self.secret_word:
            if self.kick == letter:
                self.camouflage_word[index] = letter
            index += 1

    def message_game_over(self):
        victory = False
        defeat = False

        victory = '_' not in self.camouflage_word
        defeat = self.error == 7

        if victory:
            self.message.victory_message(self.secret_word)
            self.game_over = True
        if defeat:
            self.gallows.gallows_drawing(self.error)
            self.message.defeat_message(self.secret_word)
            self.game_over = True

    def game_score(self):
        if not self.kick in self.secret_word:
            if not self.kick in self.letter:
                self.add_letter_kick(self.kick)
                self.error += 1

    def loop_game(self):
        while not self.game_over:
            self.gallows.gallows_drawing(self.error)
            print(self.camouflage_word)
            self.kick = self.valid_kick.get_letter_kicked()
            self.game_score()
            self.add_letters_to_array()
            self.message_game_over()


    def build_game(self):
        self.message.opening_message(self.max_error)
        self.secret_word = self.get_secret_word.get_secret_word()
        self.camouflage_word = self.camouflage_secret_word(self.secret_word)
        print(self.secret_word)
        self.loop_game()


startGame = Game()
startGame.build_game()
