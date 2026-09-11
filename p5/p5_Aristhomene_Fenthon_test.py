import unittest
from p5_Aristhomene_Fenthon import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesar_cipher("Hello World", 3), "Khoor Zruog")

    def test_cipher_lowercase(self):
        self.assertEqual(caesar_cipher("abc", 2), "cde")

    def test_cipher_wraparound(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")

    def test_cipher_preserves_spaces(self):
        self.assertEqual(caesar_cipher("Hello World!", 3), "Khoor Zruog!")


class TestCaesarDecipher(unittest.TestCase):

    def test_decipher(self):
        self.assertEqual(caesar_decipher("Khoor Zruog", 3), "Hello World")

    def test_decipher_wraparound(self):
        self.assertEqual(caesar_decipher("abc", 3), "xyz")


class TestLetterFrequency(unittest.TestCase):

    def test_frequency(self):
        self.assertEqual(
            letter_frequency("Hello World"),
            {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
        )

    def test_frequency_ignores_case(self):
        self.assertEqual(
            letter_frequency("AaBbCc"),
            {'a': 2, 'b': 2, 'c': 2}
        )

    def test_frequency_ignores_non_letters(self):
        self.assertEqual(
            letter_frequency("Hello! 123"),
            {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        )


if __name__ == "__main__":
    unittest.main()