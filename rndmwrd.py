import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        english_words = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский язык
        translator = Translator()
        russian_word = translator.translate(english_words, dest="ru").text
        russian_definition = translator.translate(word_definition, dest="ru").text

        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ")
        if user == russian_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()