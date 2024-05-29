import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        tranclator = Translator()

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        rus_words = tranclator.translate(english_words, dest="ru")
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        rus_definition = tranclator.translate(word_definition, dest="ru")
        # Чтобы программа возвращала словарь
        return {
            "rus_words": rus_words,
            "rus_definition": rus_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("rus_words")
        rus_definition = word_dict.get("rus_definition")

        # Начинаем игру
        print(f"Значение слова - {rus_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н")
        if play_again != "д":
            print("Спасибо за игру!")
            break


word_game()