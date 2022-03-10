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
candidates_string = ''

for candidate in candidates_list:

    candidate_str = f'id: {candidate["id"]}\n' \
                  f'name: {candidate["name"]}\n' \
                  f'picture: {candidate["picture"]}\n' \
                  f'position: {candidate["position"]}\n' \
                  f'gender: {candidate["gender"]}\n' \
                  f'age: {candidate["age"]}\n' \
                  f'skills: {candidate["skills"]}\n\n'

    candidates_string +=candidate_str

# str_candidate_list = [candidate_0]
# print(str_candidate_list[0])

# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
app = Flask(__name__)

@app.route("/")
def page_index():

    return f"<pre>{candidates_string}<pre>"

app.run()