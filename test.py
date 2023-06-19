import unittest

import classes

class TestCharacterCreation(unittest.TestCase):
    def test_single_char_creation(self):
        expected = 'A'
        real = classes.Character('A')
        self.assertEqual(expected, str(real))
    
    def test_compose_char_creation(self):
        expected = '\[ae]'
        real = classes.Character('ae')
        self.assertEqual(expected, str(real))

class TestAlphabetCreation(unittest.TestCase):
    def test_one_len_alphabet_creation(self):
        expected = '[a]'
        real = classes.Alphabet([classes.Character('a')])
        self.assertEqual(expected, str(real))
    
    def test_two_len_alphabet_creation(self):
        expected = '[a, \[ae]]'
        real = classes.Alphabet([
            classes.Character('a'),
            classes.Character('ae')
        ])
        self.assertEqual(expected, str(real))

class TsetWordCreation(unittest.TestCase):
    def test_single_char_word_creation(self):
        expected = 'hola'
        real = classes.Word([
            classes.Character('h'),
            classes.Character('o'),
            classes.Character('l'),
            classes.Character('a')
        ])

        self.assertEqual(expected, str(real))
    
    def test_compose_char_word_creation(self):
        expected = 'hol\[ae]'
        real = classes.Word([
            classes.Character('h'),
            classes.Character('o'),
            classes.Character('l'),
            classes.Character('ae')
        ])
        self.assertEqual(expected, str(real))

if __name__ == '__main__':
    unittest.main()