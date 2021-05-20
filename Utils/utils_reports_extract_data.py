import json

import requests


def get_data_from_order_logs(url: str, filter_data: dict) -> dict:
    data = {'orders': None}
    try:
        res = requests.post(url, json=filter_data)
        return_status = True
        return_msg = "ok"
        data = res.json()
    except Exception as Error:
        return_status = False
        return_msg = Error

    return dict(status=return_status, message=return_msg, data=data['orders'])


# dates = {"initial_date": '2021-05-10', "final_date": '2021-05-20'}
# a = get_data_from_order_logs(url="http://127.0.0.1:8000/orders/reports/2", filter_data=dates)
# print(a['data'])