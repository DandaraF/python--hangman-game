import string

from utils.muliple_replace import Replace


class Kick:
    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.replace = Replace()
        self.valid_kick = False

    def get_letter_kicked(self):
        while not self.valid_kick:
            print()
            kicked_letter = input('\033[32mDigite uma letra: \033[m')
            kicked_letter = kicked_letter.strip().upper()
            print()
            if kicked_letter in self.alphabet:
                return kicked_letter
            else:
                self.alphabet_error_message()

    def alphabet_error_message(self):
        print('\033[0;31mValor inválido. Digite uma letra do Alfabeto Alfanumérico.\033[m')
        print()
        print('             Alfabeto Alfanumérico:     ')
        print(self.replace.muliple_replace(self.alphabet))
        print()


kick = Kick()
kick.alphabet_error_message()


