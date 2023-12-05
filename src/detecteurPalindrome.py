import os


class DétecteurPalindrome:
    @classmethod
    def détecter(cls, chaîne):
        return 'Bonjour' + os.linesep + chaîne[::-1]
