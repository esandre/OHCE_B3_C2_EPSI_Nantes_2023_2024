from detecteurPalindrome import DétecteurPalindrome
from momentDeLaJournée import MomentDeLaJournée
from utilities.langueStub import LangueStub


class DétecteurPalindromeBuilder:
    def __init__(self):
        self.__moment = MomentDeLaJournée.INCONNU
        self.__langue = LangueStub()

    @classmethod
    def buildDefault(cls):
        return DétecteurPalindromeBuilder().build()

    def build(self):
        return DétecteurPalindrome(self.__langue, self.__moment)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self

    def ayantPourMomentDeLaJournée(self, moment):
        self.__moment = moment
        return self
