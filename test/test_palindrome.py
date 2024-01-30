import os
import unittest

from DétecteurPalindrome import DétecteurPalindrome


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        cas = ['epsi', 'test']

        # ETANT DONNE une chaîne n'étant pas un palindrome
        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = DétecteurPalindrome.détecter(chaîne)

                # ALORS on obtient son miroir
                self.assertIn(chaîne[::-1], résultat)

    def test_bien_dit(self):
        cas = ['kayak', 'radar']
        # ETANT DONNE un palindrome
        for palindrome in cas:
            with self.subTest(palindrome):
                # QUAND on vérifie si c'est un palindrome
                résultat = DétecteurPalindrome.détecter(palindrome)

                # ALORS "Bien dit" est envoyé après la réponse
                attendu = palindrome + os.linesep + "Bien dit !"
                self.assertIn(attendu, résultat)

    def test_bonjour(self):
        cas = ['kayak', 'test']

        # ETANT DONNE une chaîne
        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = DétecteurPalindrome.détecter(chaîne)

                # ALORS "Bonjour" est envoyé avant tout
                première_ligne = résultat.split(os.linesep)[0]
                self.assertEqual(première_ligne, "Bonjour")

    def test_au_revoir(self):
        cas = ['kayak', 'test']

        # ETANT DONNE une chaîne
        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = DétecteurPalindrome.détecter(chaîne)

                # ALORS "Au revoir" est envoyé en dernier
                dernière_ligne = résultat.split(os.linesep)[-1]
                self.assertEqual(dernière_ligne, "Au revoir")


if __name__ == '__main__':
    unittest.main()
