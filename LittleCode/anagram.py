'''
An anagram is defined as: “a word, phrase, or name formed by rearranging the letters of another”. 
Write a method or function that will determine if a word is an anagram. 
Ignore any characters other than a-zA-Z. Provide a way to confirm the code works as intended.
'''

import unittest


def check_anagram(check_word, test_word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for ltr in alphabet:
        if list(check_word.lower()).count(ltr) != list(test_word.lower()).count(ltr):
            return False
    return True



class TestCheckAnagram(unittest.TestCase):

    def test_basic_anagram(self):
        self.assertTrue(check_anagram("cat", "tca"))
        self.assertTrue(check_anagram("Remi", "irem"))

    def test_extra_chars(self):
        self.assertFalse(check_anagram("cat", "ccat"))
        self.assertFalse(check_anagram("Remi", "Remii"))
        self.assertFalse(check_anagram("remi", "rem"))
        self.assertFalse(check_anagram("rem", "remi"))

    def test_non_alpha_chars(self):
        self.assertTrue(check_anagram("hot-dog", "hotdog"))
        self.assertTrue(check_anagram("!___-!", ""))

    def test_mismatched_case(self):
        self.assertTrue(check_anagram("HOTdog", "hotDog"))
        self.assertTrue(check_anagram("here is A CAT", "here Is A cat"))

    def test_non_anagrams(self):
        self.assertFalse(check_anagram("Remi", "HotDog"))
        self.assertFalse(check_anagram("cat", "dog"))


if __name__ == '__main__':
    unittest.main()


