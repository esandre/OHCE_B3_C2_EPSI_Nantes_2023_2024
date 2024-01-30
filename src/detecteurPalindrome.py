import os


class DétecteurPalindrome:
    def __init__(self, langue):
        self.__langue = langue

    def détecter(self, chaîne):
        miroir = chaîne[::-1]

        début = (self.__langue.saluer()
                 + os.linesep
                 + miroir
                 + os.linesep)

        return ((début + self.__langue.féliciter()
                if chaîne == miroir
                else début)
                + "Au revoir")
