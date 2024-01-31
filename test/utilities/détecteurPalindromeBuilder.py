from detecteurPalindrome import DétecteurPalindrome
from utilities.langueStub import LangueStub


class DétecteurPalindromeBuilder:
    def __init__(self):
        self.__langue = LangueStub()

    @classmethod
    def buildDefault(cls):
        return DétecteurPalindromeBuilder().build()

    def build(self):
        return DétecteurPalindrome(self.__langue)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self
