import random


def game():

    opening_message()
    secret_word = load_word()

    correct_letters = camouflage_word(secret_word)
    print(correct_letters)

    hanged = False  # enforcou
    hit = False  # acertou
    error = 0

    while (not hanged and not hit):
        kick = next_kick()

        if (kick in secret_word):
            score_kick(kick, correct_letters, secret_word)
        else:
            error += 1
            gallows(error)

        hanged = error == 7
        hit = '_' not in correct_letters
        print(correct_letters)

    if(hit):
        victory_message()
    else:
        defeat_message(secret_word)


def gallows(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):

        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def defeat_message(secret_word):
    print()
    print("Você perdeu!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def victory_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def score_kick(kick, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if(kick == letter):
            correct_letters[index] = letter
        index += 1


def next_kick():
    print()

    kick = input('Digite uma letra: ')
    kick = kick.strip().upper()
    return kick


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
    print('           Você pode errar 7 vezes.           ')
    print('                 Boa sorte!                   ')
    print()


game()
