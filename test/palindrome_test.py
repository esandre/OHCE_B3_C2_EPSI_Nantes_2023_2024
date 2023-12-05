import os
import unittest

from detecteurPalindrome import DétecteurPalindrome


class MyTestCase(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE une chaîne
        for chaîne in ['test', 'epsi']:
            with self.subTest(chaîne):
                # QUAND je demande si elle est un palindrome
                résultat = DétecteurPalindrome.détecter(chaîne)

                # ALORS j'obtiens cette chaîne en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_bonjour(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND je demande si elle est un palindrome
        résultat = DétecteurPalindrome.détecter(chaîne)

        # ALORS la première ligne est "Bonjour"
        premiere_ligne = résultat.split(os.linesep)[0]
        self.assertEqual('Bonjour', premiere_ligne)


if __name__ == '__main__':
    unittest.main()
