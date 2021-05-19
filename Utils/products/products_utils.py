import requests

def get_all_products():
    response = requests.get("http://localhost:5000/books", headers={"Access-Key": "123456789"})
    response = response.json()

    list_response = []

    for item in response["result_data"]:
        if item["item_quantity"] == 0:
            list_response.append(item)
    return list_response
