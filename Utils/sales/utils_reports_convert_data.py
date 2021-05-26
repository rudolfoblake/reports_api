import statistics


def transform_list_of_products(unique_ids: set, list_of_products: list) -> list:
    """
    convert the list of all products in a consolidate list of products
    :param unique_ids:
    :param list_of_products:
    :return:
    """
    unique_products = []
    for index, value in enumerate(unique_ids):
        unique_products.append(dict(item_id=value, quantity_purchased=0, title="", total_price=0, prices=[]))

    for product in list_of_products:
        for index, value in enumerate(unique_products):
            if value["item_id"] == product["item_id"]:
                unique_products[index]["title"] = product["title"]
                unique_products[index]["quantity_purchased"] += product["quantity_purchased"]
                unique_products[index]["total_price"] += product['item_price']
                unique_products[index]["prices"].append(product["item_price"])
    return unique_products


def calculate_median_price(list_of_prices: list) -> list:
    """
    function that returns the median of a list of float/int values
    :param list_of_prices: list of float/int values
    :return: float value of median prices
    """
    return statistics.median(list_of_prices)


def convert_lists(log_list: list) -> tuple:
    """
    Gets the list of all products and return a set of unique ids and a list of itens
    :param log_list:
    :return:
    """
    ids = []
    list_of_products = []

    for index, value in enumerate(log_list):
        for item in value['order']['products']:
            if "item_id" in item.keys():
                list_of_products.append(item)
                ids.append(item['item_id'])

    unique_ids = set(ids)
    return unique_ids, list_of_products


def convert_log_data(log_list: list) -> list:
    """
    function that convert a list of log sales in a list by product consolidating the total quantity
    :param log_list: list of sales
    :return: list by products
    """
    unique_ids, list_of_products = convert_lists(log_list)
    unique_products = transform_list_of_products(unique_ids, list_of_products)

    for product in unique_products:
        product["median_price"] = calculate_median_price(product["prices"])
        del product["prices"]

    return sorted(unique_products, key=lambda k: k["quantity_purchased"], reverse=True)
