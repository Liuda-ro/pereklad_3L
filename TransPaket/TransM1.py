from googletrans import Translator, LANGUAGES

translator = Translator()

# Функція для перекладу тексту
def TransLate(text: str, src: str = '', dest: str = 'en') -> str:
    try:
        src_lang = LANGUAGES.get(src.lower(), src)
        dest_lang = LANGUAGES.get(dest.lower(), dest)
        trans = translator.translate(text, src=src_lang, dest=dest_lang)
        return trans.text
    except Exception as e:
        return f"Error translating text: {e}"

# Функція для визначення мови
def LangDetect(text: str, set: str = "all") -> str:
    try:
        det = translator.detect(text)
        if set == "lang":
            return det.lang
        elif set == "confidence":
            return str(det.confidence)
        elif set == "all":
            return f"Detected language: {det.lang}, confidence: {det.confidence}"
        else:
            return f"Error: invalid 'set' parameter"
    except Exception as e:
        return f"Error detecting language: {e}"

# Функція для отримання коду мови або назви мови
def CodeLang(lang: str) -> str:
    try:
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        for code, name in LANGUAGES.items():
            if name.lower() == lang.lower():
                return code
        return "Error: language not found"
    except Exception as e:
        return f"Error finding language code: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        header = ["N", "Language", "ISO-639 code","Text"]


        if out == "screen":

            print(f"{header[0]:<4} {header[1]:<20} {header[2]:<10} {header[3]:<30} \n", end="")
            print("-------------------------------------------------------------------------- \n")

            for i, (code, language) in enumerate(LANGUAGES.items(), start=1):
                row = f"{i:<4} {language:<20} {code:<10}"
                if text:
                    translated_text = translator.translate(text, dest=code).text
                    row += f" {translated_text:<30}"
                print(row)
            return "Ok"

        elif out == "file":
            with open("lan.txt", "w", encoding="utf-8") as f:
                f.write(f"{header[0]:<4} {header[1]:<20} {header[2]:<10}")
                if text:
                    f.write(f" {header[3]:<30}")
                f.write("\n" + "-" * 60 + "\n")

                for i, (code, language) in enumerate(LANGUAGES.items(), start=1):
                    row = f"{i:<4} {language:<20} {code:<10}"
                    if text:
                        translated_text = translator.translate(text, dest=code).text
                        row += f" {translated_text:<30}"
                    f.write(row + "\n")
            return "Ok"
    except Exception as e:
        return f"Error generating language list: {e}"



#print(TransLate("Dien dobry", "pl", "uk"))
#print(LangDetect("Добрий день", "all"))
#print(CodeLang("uk"))
#print(LanguageList("screen", "Добрий день"))






