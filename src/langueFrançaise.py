from momentDeLaJournée import MomentDeLaJournée


class LangueFrançaise:
    def saluer(self, moment):
        if moment == MomentDeLaJournée.SOIR or moment == MomentDeLaJournée.NUIT:
            return "Bonsoir"
        return "Bonjour"
