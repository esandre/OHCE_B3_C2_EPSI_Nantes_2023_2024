import os


class DétecteurPalindrome:
    def __init__(self, langue, moment):
        self.__moment = moment
        self.__langue = langue

    def détecter(self, chaîne):
        miroir = chaîne[::-1]

        début = (self.__langue.saluer(self.__moment)
                 + os.linesep
                 + miroir
                 + os.linesep)

        return (début + "Bien dit !" if chaîne == miroir else début) + "Au revoir"
