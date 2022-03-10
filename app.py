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

# ПЕРВЫЙ ШАГ ДЗ - выводим ВСЁ
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


# ВТОРОЙ ШАГ ДЗ - выводим кандидата по ID

def find_user_by_id(user_id):
    candidate_string = ''
    for candidate in candidates_list:
        if candidate["id"] == int(user_id):
            candidate_string += f'<img src = "{candidate["picture"]}">\n\n'
            candidate_string += f'<pre>\nИмя кандидата - {candidate["name"]}\n' \
                                 f'Позиция кандидата - {candidate["position"]}\n' \
                                 f'Навыки: {candidate["skills"]}'

            break
    else:
        candidate_string += f'<h1>Кандидат не найден</h1>'
    return candidate_string

def find_user_by_skill(skill):
    candidate_string = ''
    for candidate in candidates_list:
        skills_list = candidate["skills"].split(',')
        if skill in skills_list:
            candidate_string +=


find_user_by_skill('s')
# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
# app = Flask(__name__)
#
# @app.route("/")
# def page_index():
#     return f"<pre>{candidates_string}<pre>"
#
# @app.route("/candidate/<id>")
# def uder_id(id):
#     user_info_by_id = find_user_by_id(id)
#     return user_info_by_id
#
# @app.route("/skill/<x>")
# def user_skill(x):
#     return x
#
#
# app.run()

