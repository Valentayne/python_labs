from lab3.task1.alphabet import Alphabet
from lab3.task1.eng_alphabet import EngAlphabet

if __name__ == '__main__':
    eng = EngAlphabet()

    print("=== Літери алфавіту ===")
    eng.print_alphabet()

    print(f"\nКількість букв: {eng.letters_num()}")

    print(f"\nЧи 'J' відноситься до англійського алфавіту? {eng.is_en_letter('J')}")

    ua = Alphabet()
    print(f"Чи 'Щ' відноситься до українського алфавіту? {ua.is_ua_lang('Щ')}")

    print(f"\nПриклад тексту англійською: {EngAlphabet.example()}")