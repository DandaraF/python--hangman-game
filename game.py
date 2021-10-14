import random


def game():

    error = 0

    opening_message()
    secret_word = load_word()
    gallows(error)

    correct_letters = camouflage_word(secret_word)
    print(correct_letters)

    hanged = False
    hit = False

    letters = []

    while (not hanged and not hit):

        kick = next_kick(error)
        if (kick in secret_word):
            if (kick in letters):
                message_letters(letters, error)
            else:
                if (kick != ''):
                    letters.append(kick)
                    message_letters(letters, error)
                    score_kick(kick, correct_letters, secret_word)

        elif (kick in letters):
            message_letters(letters, error)

        else:
            letters.append(kick)
            error += 1
            message_letters(letters, error)

        hanged = error == 7
        hit = '_' not in correct_letters
        print(correct_letters)

    if(hit):
        victory_message()
    else:
        defeat_message(secret_word)


def message_letters(letters, error):
    print('___________________________________')
    print()
    print('Letras chutadas: {}'.format(letters))
    gallows(error)


def gallows(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):

        print(" |   \033[0;31m   (_)  \033[m  ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |  \033[0;31m    (_) \033[m  ")
        print(" |    \033[0;31m  \   \033[m   ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |  \033[0;31m    (_) \033[m   ")
        print(" |  \033[0;31m    \|  \033[m   ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |  \033[0;31m    (_) \033[m   ")
        print(" |  \033[0;31m    \|/ \033[m   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |  \033[0;31m    (_) \033[m   ")
        print(" |   \033[0;31m   \|/ \033[m   ")
        print(" |   \033[0;31m    |  \033[m   ")
        print(" |            ")

    if(error == 6):
        print(" | \033[0;31m     (_) \033[m   ")
        print(" |  \033[0;31m    \|/ \033[m   ")
        print(" |   \033[0;31m    |  \033[m   ")
        print(" |   \033[0;31m   /   \033[m   ")

    if (error == 7):
        print(" |  \033[0;31m    (_)  \033[m  ")
        print(" |  \033[0;31m    \|/  \033[m  ")
        print(" |  \033[0;31m     |   \033[m  ")
        print(" |  \033[0;31m    / \  \033[m  ")

    print(" |            ")
    print("_|___         ")
    print()


def defeat_message(secret_word):
    print()
    print('\033[0;31m    Você perdeu! \033[m        ')
    print('A palavra era \033[0;31m{}'.format(secret_word))
    print(' \033[0;31m__________________________ ')
    print('|                          |')
    print('|      * GAMER OVER *      |')
    print('|__________________________|\033[m')


def victory_message():
    print()
    print(" \033[32mParabéns, você ganhou! ")
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


def score_kick(kick, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if(kick == letter):
            correct_letters[index] = letter
        index += 1


def next_kick(error):
    characteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    valid_kick = ''

    while (not valid_kick):
        print()
        kick = input('\033[32mDigite uma letra: \033[m')
        print()
        kick = kick.strip().upper()
        if (kick in characteres):
            valid_kick = kick
        else:
            print(
                '\033[0;31mValor inválido. Digite uma letra do alfabeto.\033[m')
            print()
            print('Alfabeto: {}'.format(characteres))
            print()
            gallows(error)
        return valid_kick


def camouflage_word(secret_word):
    return ['_' for line in secret_word]


def load_word():
    file = open('words.txt', 'r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()

    return secret_word


def opening_message():
    print('**********************************************')
    print('**********Bem vindo ao jogo da Forca!*********')
    print('**********************************************')
    print()
    print('           Você pode errar 7 vezes.           ')
    print('                 Bom jogo!                    ')
    print()


game()
