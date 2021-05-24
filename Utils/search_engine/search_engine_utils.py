import requests
import operator

GET_LOGGED_USERS_REPORT = 1
GET_NOT_LOGGED_USERS_REPORT = 0
SEARCH_TYPE_LIST = [GET_LOGGED_USERS_REPORT, GET_NOT_LOGGED_USERS_REPORT]


# Pega todos as buscas de usuários logados e não logados de acrodo com a Constante informada (search_type).
def get_all_searches(dates, search_type):
    response = requests.post("http://127.0.0.1:5000/get_all_searches", json=dates)
    response = response.json()
    searches_list = []

    if search_type == GET_LOGGED_USERS_REPORT:
        for item in response:
            if "user_id" in item.keys():
                searches_list.append(item)
    elif search_type == GET_NOT_LOGGED_USERS_REPORT:
        for item in response:
            if not "user_id" in item.keys():
                searches_list.append(item)
    return searches_list


# Recebe a lista de pesquisas, e de acordo com search_type retorna as categorias dos logados e não logados.
def get_categories(dates, search_type):
    category_list = []
    if search_type == GET_LOGGED_USERS_REPORT:
        searches_list = get_all_searches(dates, search_type)
        for item in searches_list:
            if "category" in item.keys():
                category_list.append(item["category"])

    elif search_type == GET_NOT_LOGGED_USERS_REPORT:
        searches_list = get_all_searches(dates, search_type)
        for item in searches_list:
                if "category" in item.keys():
                    category_list.append(item["category"])
    return category_list


# Converte a lista de listas das categorias, para uma lista de strings.
def convert_category_to_string_list(list_values):
    list_of_strings_only = []

    for l in list_values:
        for c in l:
            list_of_strings_only.append(c)

    return list_of_strings_only


# Conta quantas incidencias tem de cada string.
def string_count(list_to_count):
    counted_categories = {i: list_to_count.count(i) for i in list_to_count}
    return counted_categories


# Busca os relatórios requisitados, pela data inicial e final informada,
# e pela search_type que separa logados de não logados.
def get_reports(dates, search_type):
    if search_type not in SEARCH_TYPE_LIST:
        return False, []
    elif search_type == GET_LOGGED_USERS_REPORT:
        try:
            total_list = get_categories(dates, search_type)
            converted_list = convert_category_to_string_list(total_list)
            counted_list = string_count(converted_list)
            counted_list = sorted(counted_list.items(), key=operator.itemgetter(1), reverse=True)
            return True, counted_list
        except Exception as error:
            return False, f"Error: {error}"
    elif search_type == GET_NOT_LOGGED_USERS_REPORT:
        try:
            total_list = get_categories(dates, search_type)
            converted_list = convert_category_to_string_list(total_list)
            counted_list = string_count(converted_list)
            counted_list = sorted(counted_list.items(), key=operator.itemgetter(1), reverse=True)
            return True, counted_list
        except Exception as error:
            return False, f"Error: {error}"
