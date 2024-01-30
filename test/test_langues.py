import unittest

from langueAnglaise import LangueAnglaise
from langueFrançaise import LangueFrançaise


class TestLangues(unittest.TestCase):
    def test_félicitations(self):
        cas = [[LangueFrançaise(), 'Bien dit !'], [LangueAnglaise(), 'Well said !']]

        for paramètres in cas:
            langue = paramètres[0]
            félicitation_attendue = paramètres[1]
            with (self.subTest(str(langue) + ':' + félicitation_attendue)):
                # ETANT DONNE une <langue>
                # QUAND on félicite
                félicitations = langue.féliciter()

                # ALORD on obtient les salutations de cette langue
                self.assertEqual(félicitation_attendue, félicitations)
