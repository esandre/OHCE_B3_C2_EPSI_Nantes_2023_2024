import os


class DétecteurPalindrome:
    def __init__(self, langue):
        self.__langue = langue
        pass

    def détecter(self, chaîne):
        miroir = chaîne[::-1]

        début = (self.__langue.saluer()
                 + os.linesep
                 + miroir
                 + os.linesep)

        return (début + "Bien dit !" if chaîne == miroir else début) + "Au revoir"
