import requests

def get_all_searches_by_user_not_logged():
    response = requests.get("http://127.0.0.1:5000/get_all_searches")
    response = response.json()
    not_logged_list = []
    for item in response:
        try:
            if not item["user_id"] in response:
                not_logged_list.append(item)
        except KeyError:
            pass
    return not_logged_list



x = get_all_searches_by_user_not_logged()
print(x)