class Message:

    def __init__(self):
        self.letters = []

    def opening_message(self, error):
        print('**********************************************')
        print('*         Bem vindo ao jogo da Forca!        *')
        print('**********************************************')
        print()
        print(f'           Você pode errar {error} vezes.           ')
        print('                 Bom jogo!                    ')
        print()

    def message_letters(self, letter):
        self.letters.append(letter)
        print('_________________________________________________________________')
        print()
        print('Letras chutadas: {}'.format(self.letters))

    def victory_message(self, secret_word):
        print()
        print(" \033[32mParabéns, você ganhou! ")
        print(f"   Palavra secreta é {secret_word} ")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       \033[m")

    def defeat_message(self, secret_word):
        print()
        print('\033[0;31m    Você perdeu! \033[m        ')
        print('A palavra é \033[0;31m{}'.format(secret_word))
        print(' \033[0;31m__________________________ ')
        print('|                          |')
        print('|      * GAMER OVER *      |')
        print('|__________________________|\033[m')
