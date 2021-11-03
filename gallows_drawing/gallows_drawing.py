class Gallows:
    def gallows_drawing(self, error):
        print("  _______     ")
        print(" |/      |    ")

        if (error == 1):
            print(" |   \033[0;31m   (_)  \033[m  ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (error == 2):
            print(" |  \033[0;31m    (_) \033[m  ")
            print(" |    \033[0;31m  \   \033[m   ")
            print(" |            ")
            print(" |            ")

        if (error == 3):
            print(" |  \033[0;31m    (_) \033[m   ")
            print(" |  \033[0;31m    \|  \033[m   ")
            print(" |            ")
            print(" |            ")

        if (error == 4):
            print(" |  \033[0;31m    (_) \033[m   ")
            print(" |  \033[0;31m    \|/ \033[m   ")
            print(" |            ")
            print(" |            ")

        if (error == 5):
            print(" |  \033[0;31m    (_) \033[m   ")
            print(" |   \033[0;31m   \|/ \033[m   ")
            print(" |   \033[0;31m    |  \033[m   ")
            print(" |            ")

        if (error == 6):
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
