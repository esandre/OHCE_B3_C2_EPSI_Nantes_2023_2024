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
                self.assertEqual(attendu, résultat)


if __name__ == '__main__':
    unittest.main()
