
from googletrans import Translator
import os
translator = Translator()
config_file='inform.txt'

def read_config(config_file):
    config = {}
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо пробіли навколо знака '='
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Файл '{config_file}' не знайдено")
    return config

def analyze_text(file_path, max_chars, max_words, max_sentences):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Аналіз тексту
        sentences = text.split('.')
        words = text.split()
        chars = len(text)

        return {
            'text': text,
            'chars': chars,
            'words': len(words),
            'sentences': len(sentences)
        }
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено!")
        return None

def main():
    # Зчитуємо конфігураційний файл
    config = read_config(config_file)

    # Перевіряємо наявність необхідних параметрів
    file_name = config.get('file_name')
    cod_lang = config.get('cod_lang', 'uk')
    vyvid = config.get('vyvid', 'screen')
    count_sym = int(config.get('count_sym', 600))
    word = int(config.get('word', 100))
    rech = int(config.get('rech', 10))

    if not file_name:
        print("Помилка: В конфігураційному файлі не вказано ім'я текстового файлу.")
        return

    # Аналізуємо текстовий файл
    stats = analyze_text(file_name, count_sym, word, rech)
    if stats is None:
        return

    print(f"\nНазва файлу: {file_name}")
    print(f"Розмір файлу: {os.path.getsize(file_name)} байт")
    print(f"Кількість символів: {stats['chars']}")
    print(f"Кількість слів: {stats['words']}")
    print(f"Кількість речень: {stats['sentences']}")

    # Перекладаємо текст із використанням Google Translate
    text_to_translate = stats['text']
    try:
        translated = translator.translate(text_to_translate, src='auto', dest=cod_lang).text
    except Exception as e:
        print(f"Помилка перекладу: {e}")
        return

    # Виводимо результат
    if vyvid == 'screen':
        print("\nПереклад:")
        print(translated)
    elif vyvid == 'file':
        output_file = f"{file_name.split('.')[0]}_{cod_lang}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated)
            print(f"\nПереклад збережено у файл: {output_file}")
        except Exception as e:
            print(f"Помилка запису у файл: {e}")
    else:
        print("Помилка! Невірне значення параметра 'vyvid'.")

if __name__ == '__main__':
    main()
