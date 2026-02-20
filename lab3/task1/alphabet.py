class Alphabet:
    default_lang = 'Ua'
    default_letters = list('АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя')

    def __init__(self, lang=None, letters=None):
        self.lang = lang if lang is not None else Alphabet.default_lang
        self.letters = letters if letters is not None else Alphabet.default_letters

    def print_alphabet(self):
        print(f"Алфавіт мови '{self.lang}':")
        print(' '.join(self.letters))

    def letters_num(self):
        return len(self.letters)

    def is_ua_lang(self, text):
        ua_set = set('АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
        text_letters = set(c for c in text if c.isalpha())
        return bool(text_letters) and text_letters.issubset(ua_set)

