import os


class DétecteurPalindrome:
    @classmethod
    def détecter(cls, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        début = "Bonjour" + os.linesep
        fin = os.linesep + "Au revoir"

        milieu = miroir + os.linesep + "Bien dit !" \
            if est_palindrome \
            else miroir

        return début + milieu + fin
