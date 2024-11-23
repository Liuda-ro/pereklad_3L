from TransPaket.TransM2 import LangDetect, TransLate, CodeLang, LanguageList


def main():
    text = "Dzien dobry"
    src = "pl"
    dest = "en"  # вказав мову призначення
    set = "all"
    out = "screen"

    # Визначення мови тексту
    det = LangDetect(text, set=set)
    print(det)

    # Переклад тексту
    trans = TransLate(text, src=src, dest=dest)
    print(trans)

    # Отримання коду мови
    cod = CodeLang(src)
    print(f"Language code for '{dest}': {cod}")

    # Виведення списку мов
    lis = LanguageList(out, text)
    print(lis)

# Виконання головної функції
if __name__ == '__main__':
    main()