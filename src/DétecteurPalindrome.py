import os


class DétecteurPalindrome:
    @classmethod
    def détecter(cls, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        début = "Bonjour" + os.linesep

        return début + miroir + os.linesep + "Bien dit !" \
            if est_palindrome \
            else début + miroir
