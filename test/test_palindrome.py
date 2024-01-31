import os
import unittest

from langueAnglaise import LangueAnglaise
from langueFrançaise import LangueFrançaise
from momentDeLaJournée import MomentDeLaJournée
from utilities.détecteurPalindromeBuilder import DétecteurPalindromeBuilder

cas_test_non_palindrome = ['test', 'epsi']


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE une chaîne
        for chaîne in cas_test_non_palindrome:
            with self.subTest(chaîne):
                # QUAND je demande si elle est un palindrome
                résultat = DétecteurPalindromeBuilder.buildDefault().détecter(chaîne)

                # ALORS j'obtiens cette chaîne en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_bien_dit(self):
        # ETANT DONNE un palindrome
        palindrome = 'radar'

        # QUAND on le fournit au détecteur
        résultat = DétecteurPalindromeBuilder.buildDefault().détecter(palindrome)

        # ALORS on obtient cette chaîne suivie de "Bien dit !"
        attendu = palindrome + os.linesep + 'Bien dit !'
        self.assertIn(attendu, résultat)

    def test_absence_bien_dit(self):
        # ETANT DONNE un non-palindrome
        for chaîne in cas_test_non_palindrome:
            with self.subTest(chaîne):
                # QUAND on le fournit au détecteur
                résultat = DétecteurPalindromeBuilder.buildDefault().détecter(chaîne)

                # ALORS "Bien dit !" n'apparaît pas
                self.assertNotIn('Bien dit !', résultat)

    def test_saluer(self):
        cas = [
            [LangueFrançaise(), 'Bonjour', MomentDeLaJournée.INCONNU],
            [LangueFrançaise(), 'Bonjour', MomentDeLaJournée.MATIN],
            [LangueFrançaise(), 'Bonjour', MomentDeLaJournée.APRES_MIDI],
            [LangueFrançaise(), 'Bonsoir', MomentDeLaJournée.SOIR],
            [LangueFrançaise(), 'Bonsoir', MomentDeLaJournée.NUIT],
            [LangueAnglaise(), 'Hello', MomentDeLaJournée.INCONNU],
            [LangueAnglaise(), 'Good Morning', MomentDeLaJournée.MATIN],
            [LangueAnglaise(), 'Good Afternoon', MomentDeLaJournée.APRES_MIDI],
            [LangueAnglaise(), 'Good Evening', MomentDeLaJournée.SOIR],
            [LangueAnglaise(), 'Good Night', MomentDeLaJournée.NUIT],
        ]

        for paramètres in cas:
            langue = paramètres[0]
            salutations_attendues = paramètres[1]
            moment = paramètres[2]
            with self.subTest(str(langue) + ':' + salutations_attendues):
                # ETANT DONNE une chaîne
                chaîne = 'test'

                # ET que l'utilisateur parle <langue>
                # ET que nous sommes à un moment de la journée inconnu
                détecteur = (DétecteurPalindromeBuilder()
                             .ayantPourLangue(langue)
                             .ayantPourMomentDeLaJournée(moment)
                             .build())

                # QUAND je demande si elle est un palindrome
                résultat = détecteur.détecter(chaîne)

                # ALORS la première ligne est la salutation de cette langue à ce moment de la journée
                premiere_ligne = résultat.split(os.linesep)[0]
                self.assertEqual(salutations_attendues, premiere_ligne)

    def test_au_revoir(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND je demande si elle est un palindrome
        résultat = DétecteurPalindromeBuilder.buildDefault().détecter(chaîne)

        # ALORS la dernière ligne est "Au revoir"
        lignes = résultat.split(os.linesep)
        dernière_ligne = lignes[-1]
        self.assertEqual('Au revoir', dernière_ligne)


if __name__ == '__main__':
    unittest.main()
