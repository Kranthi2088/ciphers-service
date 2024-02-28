from django.test import TestCase
from .ciphers import ceaser_encode

class CiphersTest(TestCase):
    def test_ceasar_encoding_1(self):
        plain_text ='hello'
        shift = 1
        expected='ifmmp'
        output=ceaser_encode(plain_text,shift)
        self.assertEqual(expected,output)
    def test_ceaser_encoding_2(self):
        plain_text='winter'
        shift = 3
        expected='zlqwhu'
        output = ceaser_encode(plain_text,shift)
        self.assertEqual(expected,output)
    def test_ceasar_encoding_3(self):
        plain_text = 'z'
        shift = 1
        expected = 'a'  
        output = ceaser_encode(plain_text, shift)
        self.assertEqual(expected, output)

