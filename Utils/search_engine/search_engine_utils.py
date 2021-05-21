import requests
from flask import request

# Pega todos as buscas de usuários não logados


def get_all_searches_by_not_loged_user(dates: dict):

    response = requests.post("http://127.0.0.1:5000/get_all_searches", json=dates)
    response = response.json()
    not_logged_user_list = []
    for item in response:
        try:
            if item["user_id"]:
                pass
        except KeyError:
            not_logged_user_list.append(item)
    return not_logged_user_list


# Pega todos as buscas de usuários logados
def get_all_searches_by_logged_users(dates: dict):
    response = requests.get("http://127.0.0.1:5000/get_all_searches")
    response = response.json()
    logged_user_list = []
    for item in response:
        try:
            if item["user_id"]:
                logged_user_list.append(item)
        except KeyError:
            pass
    return logged_user_list


# Pega as categorias da lista de usuarios não logados
def get_categories_of_not_logged_users(dates):
    category_list = []
    searches_list = get_all_searches_by_not_loged_user(dates)
    for item in searches_list:
        try:
            if item["category"]:
                category_list.append(item["category"])
        except KeyError:
            pass
    return category_list


# Pega as categorias da lista de usuarios logados
def get_categories_of_logged_users():
    category_list = []
    searches_list = get_all_searches_by_logged_user()
    for item in searches_list:
        try:
            if item["category"]:
                category_list.append(item["category"])
        except KeyError:
            pass
    return category_list


# Converte a lista de listas das categorias, para uma lista de strings
def convert_category_to_string_list(list_values):
    list_of_strings_only = []

    for l in list_values:
        for c in l:
            list_of_strings_only.append(c)
    return list_of_strings_only

# Conta quantas incidencias tem de cada string
def string_count(list_to_count):
    my_dict = {i: list_to_count.count(i) for i in list_to_count}
    return my_dict


def get_not_logged_users_report(dates):
    total_list = get_categories_of_not_logged_users(dates)
    converted_list = convert_category_to_string_list(total_list)
    counted_list = string_count(converted_list)
    return counted_list


def get_logged_users_report():
    pass


# dates = {"initial_date": "2020-01-01","final_date": "2021-12-01" }
