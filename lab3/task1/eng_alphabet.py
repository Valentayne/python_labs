from lab3.task1.alphabet import Alphabet


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self):
        super().__init__(
            lang='En',
            letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        )

    def is_en_letter(self, s):
        return s.lower() in 'abcdefghijklmnopqrstuvwxyz' and len(s) == 1

    def letters_num(self):
        return EngAlphabet.__en_letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."