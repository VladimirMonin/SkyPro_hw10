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

candidate_0 = f'id: {candidates_list[0]["id"]}\n' \
              f'name: {candidates_list[0]["name"]}\n' \
              f'picture: {candidates_list[0]["picture"]}\n' \
              f'position: {candidates_list[0]["position"]}\n' \
              f'gender: {candidates_list[0]["gender"]}\n' \
              f'age: {candidates_list[0]["age"]}\n' \
              f'skills: {candidates_list[0]["skills"]}'

str_candidate_list = [candidate_0]
print(str_candidate_list[0])

# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
app = Flask(__name__)

@app.route("/")
def page_index():

    return f"<pre>{str_candidate_list[0]}<pre>"

app.run()