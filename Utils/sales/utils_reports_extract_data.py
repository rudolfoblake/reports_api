import requests


def get_data_from_order_logs(url: str, filter_data: dict) -> dict:
    data = {'orders': None}
    headers = {'content-type': 'application/json',
               'Key': "eadc34b8d3d1463097e6df66dfabd462"}
    try:
        res = requests.post(url, json=filter_data, headers=headers)
        return_status = True
        return_msg = "ok"
        data = res.json()
    except Exception as Error:
        return_status = False
        return_msg = Error

    return dict(status=return_status, message=return_msg, data=data['orders'])
