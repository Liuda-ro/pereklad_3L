from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs


translator = GoogleTranslator()

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=src, target=dest)
        trans = translator.translate(text)
        return trans
    except Exception as e:
        return f"Error translating text: {e}"



def LangDetect(txt: str, set: str = "all") -> str:
    try:
        det = detect_langs(txt)[0]  # Отримуємо перший елемент із списку
        if set == "lang":
            return det.lang
        elif set == "confidence":
            return str(det.prob)
        elif set == "all":
            return f"Detected language: {det.lang}, confidence: {det.prob:.2f}"
        else:
            return "Error: invalid 'set' parameter"
    except Exception as e:
        return f"Error detecting language: {e}"


def CodeLang(lang: str) -> str:
    try:
        det=detect(lang)
        lang_list = translator.get_supported_languages(as_dict=True)
        if det in lang_list:
            return lang_list[det]
        elif lang in lang_list.values():
            for code, name in lang_list.items():
                if name == lang:
                    return f"Код мови{code}"
        return "Error: Language not found"
    except Exception as e:
        return f"Error in CodeLang function: {e}"


def LanguageList(out: str = "screen", text: str = "") -> str:

    try:
        # Ініціалізуємо перекладач
        translator = GoogleTranslator()

        # Отримуємо список підтримуваних мов
        lang_list = translator.get_supported_languages(as_dict=True)
        header = ["N", "Language", "ISO-639 code", "Text"]

        # Вивід на екран
        if out == "screen":
            print(f"{header[0]:<4} {header[1]:<20} {header[2]:<10} {header[3]:<30}\n")
            print("-" * 60)

            for i, (code, language) in enumerate(lang_list.items(), start=1):
                row = f"{i:<4} {language:<20} {code:<10}"

                if text:
                    translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                    row += f" {translated_text:<30}"

                print(row)

            return "Ok"

        # Запис у файл
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write(f"{header[0]:<4} {header[1]:<20} {header[2]:<10} {header[3]:<30}\n")
                f.write("-" * 60 + "\n")

                for i, (code, language) in enumerate(lang_list.items(), start=1):
                    row = f"{i:<4} {language:<20} {code:<10}"

                    if text:
                        translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                        row += f" {translated_text:<30}"

                    f.write(row + "\n")

            return "Ok"

        else:
            return "Error: Unsupported output option"

    except Exception as e:
        return f"Error generating language list: {e}"



print(TransLate("Dien dobry", "pl", "uk"))
print(LangDetect("Добрий день", "all"))
print(CodeLang("uk"))
print(LanguageList("screen", "Добрий день"))