import unittest
import numpy as np
from pysent3.hiv4 import HIV4
from pysent3.lm import LM


class TestDict(unittest.TestCase):

    def setUp(self):
        self.text = '''The Pandora papers represent the latest – and largest in terms of data volume – in a series of 
        major leaks of financial data that have convulsed the offshore world since 2013. Setting up or benefiting from 
        offshore entities is not itself illegal, and in some cases people may have legitimate reasons, such as security,
        for doing so. But the secrecy offered by tax havens has at times proven attractive to tax evaders, fraudsters
        and money launderers, some of whom are exposed in the files.
        
        The Pandora papers also place a revealing spotlight on the offshore system itself. In a development likely to 
        prove embarrassing for the US president, Joe Biden, who has pledged to lead efforts internationally to bring 
        transparency to the global financial system, the US emerges from the leak as a leading tax haven. The files 
        suggest the state of South Dakota, in particular, is sheltering billions of dollars in wealth linked to 
        individuals previously accused of serious financial crimes.'''

    def test_hiv4(self):
        hiv4 = HIV4()
        tokens = hiv4.tokenize(self.text)
        score = hiv4.get_score(tokens)
        self.assertEqual(score['Positive'], 19)
        self.assertEqual(score['Negative'], 13)
        self.assertTrue(np.isclose(score['Polarity'], 0.1875))
        self.assertTrue(np.isclose(score['Subjectivity'], 0.19999999))

    def test_lm(self):
        lm = LM()
        tokens = lm.tokenize(self.text)
        score = lm.get_score(tokens)
        self.assertEqual(score['Positive'], 6)
        self.assertEqual(score['Negative'], 8)
        self.assertTrue(np.isclose(score['Polarity'], -0.14285714))
        self.assertTrue(np.isclose(score['Subjectivity'], 0.08749999))


if __name__ == "__main__":
    unittest.main()
