import os
import unittest

from langueAnglaise import LangueAnglaise
from langueFrançaise import LangueFrançaise
from utilities.detecteurPalindromeBuilder import DétecteurPalindromeBuilder
from utilities.langueSpy import LangueSpy

cas_test_non_palindrome = ['test', 'epsi']


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE une chaîne
        for chaîne in cas_test_non_palindrome:
            with (self.subTest(chaîne)):
                # QUAND je demande si elle est un palindrome
                détecteur = DétecteurPalindromeBuilder().build()
                résultat = détecteur.détecter(chaîne)

                # ALORS j'obtiens cette chaîne en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_félicitations(self):
        cas = [[LangueFrançaise(), 'Bien dit !'], [LangueAnglaise(), 'Well said !']]

        for paramètres in cas:
            with (self.subTest(paramètres[0])):
                # ETANT DONNE un palindrome
                # ET que l'utilisateur parle <langue>
                langue = paramètres[0]
                palindrome = 'radar'

                # QUAND on le fournit au détecteur
                résultat = (DétecteurPalindromeBuilder()
                            .ayantPourLangue(langue)
                            .build()
                            .détecter(palindrome))

                # ALORS on obtient cette chaîne suivie des félicitations en <langue>
                félicitations = paramètres[1]
                attendu = palindrome + os.linesep + félicitations
                self.assertIn(attendu, résultat)

    def test_absence_bien_dit(self):
        # ETANT DONNE un non-palindrome
        for chaîne in cas_test_non_palindrome:
            with self.subTest(chaîne):
                langue = LangueSpy()
                détecteur = DétecteurPalindromeBuilder().ayantPourLangue(langue).build()

                # QUAND on le fournit au détecteur
                détecteur.détecter(chaîne)

                # ALORS aucune salutation n'apparaît
                self.assertFalse(langue.félicitationsConsultées())

    def test_saluer(self):
        cas = [[LangueFrançaise(), 'Bonjour'], [LangueAnglaise(), 'Hello']]

        for paramètres in cas:
            langue = paramètres[0]
            salutations_attendues = paramètres[1]
            with self.subTest(str(langue) + ':' + salutations_attendues):
                # ETANT DONNE une chaîne
                chaîne = 'test'

                # ET que l'utilisateur parle <langue>
                détecteur = DétecteurPalindromeBuilder().ayantPourLangue(langue).build()

                # QUAND je demande si elle est un palindrome
                résultat = détecteur.détecter(chaîne)

                # ALORS la première ligne est la salutation de cette langue
                premiere_ligne = résultat.split(os.linesep)[0]
                self.assertEqual(salutations_attendues, premiere_ligne)

    def test_au_revoir(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND je demande si elle est un palindrome
        résultat = DétecteurPalindromeBuilder().build().détecter(chaîne)

        # ALORS la dernière ligne est "Au revoir"
        lignes = résultat.split(os.linesep)
        dernière_ligne = lignes[-1]
        self.assertEqual('Au revoir', dernière_ligne)


if __name__ == '__main__':
    unittest.main()
