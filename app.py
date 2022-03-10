from flask import Flask
import json

def load_candidates(filename='candidates.json'):
    """
    Функция читает json с вопросами и возвращает словарь для игры
    :param filename: По умолчанию questions.json
    :return: Словарь
    """
    file = open(filename, encoding='UTF-8')
    candidates_list = json.load(file)
    file.close()
    return candidates_list


# ЗАГРУЗКА ВОПРОСОВ
candidates_list = load_candidates()


# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
app = Flask(__name__)

@app.route("/")
def page_index():

    return str(candidates_list[0]['name'])

app.run()