import os


class DétecteurPalindrome:
    @classmethod
    def détecter(cls, chaîne):
        miroir = chaîne[::-1]

        début = ('Bonjour'
                 + os.linesep
                 + miroir
                 + os.linesep)

        return (début + "Bien dit !" if chaîne == miroir else début) + "Au revoir"
