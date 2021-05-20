import requests


def get_all_products_with_empty_stock():
    response = requests.get("http://localhost:5000/books", headers={"Access-Key": "123456789"})
    response = response.json()
    list_response = []
    for item in response["result_data"]:
        if item["item_quantity"] == 0:
            list_response.append(item)
    return list_response


def get_all_products():
    response = requests.get("http://localhost:5000/books", headers={"Access-Key": "123456789"})
    response = response.json()
    return response


def calculate_profit_by_product(data_values):
    list_response = []
    for item in data_values["result_data"]:
        if item["item_price"] and item["item_cost_price"]:
            margin = item["item_price"] - item["item_cost_price"]
            item["profit_margin"] = margin / item["item_cost_price"] * 100
            total_margin = round(item["profit_margin"], 2)
            item["profit_margin"] = f"{total_margin}%"
            list_response.append(item)
    print(list_response)
    return list_response

