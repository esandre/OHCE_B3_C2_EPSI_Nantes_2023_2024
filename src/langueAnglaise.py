from momentDeLaJournée import MomentDeLaJournée


class LangueAnglaise:
    def saluer(self, moment):
        if moment == MomentDeLaJournée.MATIN:
            return "Good Morning"
        if moment == MomentDeLaJournée.APRES_MIDI:
            return "Good Afternoon"
        if moment == MomentDeLaJournée.SOIR:
            return "Good Evening"
        if moment == MomentDeLaJournée.NUIT:
            return "Good Night"

        return "Hello"
