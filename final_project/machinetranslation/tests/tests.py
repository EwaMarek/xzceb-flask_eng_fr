import unittest
from machinetranslation import translator

class TestEnglishToFrench(unittest.TestCase):
    """ A class to test english to french translation """
    def test_null(self):
        """ Test function behaviour when empty string passed to the function """
        self.assertEqual(translator.english_to_french(""), "")
    def test_greetings_translation(self):
        """ Test function behaviour for a basic greeting """
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    """ A class to test french to english translation """
    def test_null(self):
        """ Test function behaviour when empty string passed to the function """
        self.assertEqual(translator.french_to_english(""), "")
    def test_greetings_translation(self):
        """ Test function behaviour for a basic greeting """
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()
