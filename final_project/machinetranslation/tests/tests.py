import unittest
from machinetranslation.translator.translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Day"), "Jour")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Jour"), "Day")


if __name__ == '__main__':
    unittest.main()
