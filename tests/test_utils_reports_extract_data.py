import json
from unittest import TestCase, mock
from Utils.sales.utils_reports_extract_data import get_data_from_order_logs


class TestUtilsSalesExtractData(TestCase):

    def test_get_data_from_logs_work_with_false(self):
        my_url = "my_url"
        dates = dict(initial_date="2021-05-10", final_date="2021-05-21")
        self.assertFalse(get_data_from_order_logs(url=my_url, filter_data=dates)["status"])

    @mock.patch("Utils.sales.utils_reports_extract_data.requests")
    def test_get_data_from_logs_work(self, mock_requests):
        my_url = "my_url"
        dates = dict(initial_date="2021-05-10", final_date="2021-05-21")

        expected_result = '{"orders": "[\\n  {\\n    ' \
                          '\\"_id\\": {\\n      \\"$oid\\": \\"60a3f9ef9f5cf6c89b8f22f1\\"\\n    },\\n    ' \
                          '\\"order\\": {\\n      \\"products\\": [\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3f\\",\\n          ' \
                          '\\"title\\": \\"Harry Potter e a Camara Secreta Volume I\\",\\n          ' \
                          '\\"item_price\\": 10,\\n          ' \
                          '\\"quantity_purchased\\": 1\\n        },\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3g\\",\\n          ' \
                          '\\"title\\": \\"Percy Jackson e os Olimpianos\\",\\n          ' \
                          '\\"item_price\\": 5,\\n          ' \
                          '\\"quantity_purchased\\": 2\\n        },\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3h\\",\\n          ' \
                          '\\"title\\": \\"Biblia\\",\\n          ' \
                          '\\"item_price\\": 5,\\n          ' \
                          '\\"quantity_purchased\\": 500\\n        }\\n      ],\\n      ' \
                          '\\"user\\": {\\n        \\"user_id\\": {\\n          ' \
                          '\\"$oid\\": \\"60a3f9ef9f5cf6c89b8f22f1\\"\\n        },\\n        ' \
                          '\\"address\\": {\\n          ' \
                          '\\"address_state\\": \\"RJ\\"\\n        }\\n      },\\n      ' \
                          '\\"method\\": \\"bill\\",\\n      ' \
                          '\\"shipping_price\\": 30.0,\\n      ' \
                          '\\"total\\": 50.0,\\n      ' \
                          '\\"status\\": \\"waiting bill\\",\\n      ' \
                          '\\"bill\\": {\\n        ' \
                          '\\"due_date\\": \\"2021-05-21\\",\\n        ' \
                          '\\"documment_date\\": \\"2021-05-18\\",\\n        ' \
                          '\\"value\\": 50.0,\\n       ' \
                          '\\"barcode\\": \\"23700.99999 05182021.143127 36699909765630712916200499955716015823\\"\\n' \
                          '      },\\n      \\"message\\": \\"ok\\"\\n    },\\n    ' \
                          '\\"created_at\\": \\"2021-05-18 12:46:44.524000\\",\\n    ' \
                          '\\"updated_at\\": \\"2021-05-18 12:46:44.524690\\"\\n  },\\n  {\\n    ' \
                          '\\"_id\\": {\\n      \\"$oid\\": \\"60a3fad49f5cf6c89b8f22f4\\"\\n    },\\n    ' \
                          '\\"order\\": {\\n      \\"products\\": [\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3f\\",\\n          ' \
                          '\\"title\\": \\"Harry Potter e a Camara Secreta Volume I\\",\\n          ' \
                          '\\"item_price\\": 10,\\n          ' \
                          '\\"quantity_purchased\\": 1\\n        },\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3g\\",\\n          ' \
                          '\\"title\\": \\"Percy Jackson e os Olimpianos\\",\\n          ' \
                          '\\"item_price\\": 5,\\n          ' \
                          '\\"quantity_purchased\\": 2\\n        },\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3h\\",\\n          ' \
                          '\\"title\\": \\"Biblia\\",\\n          ' \
                          '\\"item_price\\": 5,\\n          ' \
                          '\\"quantity_purchased\\": 500\\n        }\\n      ],\\n      ' \
                          '\\"user\\": {\\n        \\"user_id\\": {\\n          ' \
                          '\\"$oid\\": \\"60a3fad49f5cf6c89b8f22f4\\"\\n        },\\n        ' \
                          '\\"address\\": {\\n          ' \
                          '\\"address_state\\": \\"RJ\\"\\n        }\\n      },\\n      ' \
                          '\\"shipping_price\\": 30.0,\\n      ' \
                          '\\"method\\": \\"credit\\",\\n      \\"card\\": {\\n        ' \
                          '\\"number\\": \\"344604579207048\\",\\n        ' \
                          '\\"month\\": \\"05\\",\\n        \\"year\\": \\"2021\\",\\n        ' \
                          '\\"cvc\\": 336,\\n        \\"brand\\": \\"American Express\\"\\n      },\\n      ' \
                          '\\"total\\": 50.0,\\n      \\"status\\": \\"paid\\",\\n      ' \
                          '\\"message\\": \\"ok\\"\\n    },\\n    ' \
                          '\\"created_at\\": \\"2021-05-18 12:46:44.524000\\",\\n    ' \
                          '\\"updated_at\\": \\"2021-05-18 12:46:44.524690\\"\\n  },\\n  {\\n    ' \
                          '\\"_id\\": {\\n      \\"$oid\\": \\"60a3fb079f5cf6c89b8f22f7\\"\\n    },\\n    ' \
                          '\\"order\\": {\\n      \\"products\\": [\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3f\\",\\n          ' \
                          '\\"title\\": \\"Harry Potter e a Camara Secreta Volume I\\",\\n          ' \
                          '\\"item_price\\": 10,\\n          ' \
                          '\\"quantity_purchased\\": 1\\n        },\\n        {\\n          ' \
                          '\\"item_id\\": \\"60a3g\\",\\n          ' \
                          '\\"title\\": \\"Percy Jackson e os Olimpianos\\",\\n          ' \
                          '\\"item_price\\": 5,\\n          ' \
                          '\\"quantity_purchased\\": 2\\n        }\\n      ],\\n      ' \
                          '\\"user\\": {\\n        \\"user_id\\": {\\n          ' \
                          '\\"$oid\\": \\"60a3fb079f5cf6c89b8f22f7\\"\\n        },\\n        ' \
                          '\\"address\\": {\\n          \\"address_state\\": \\"AC\\"\\n        }\\n      },\\n      ' \
                          '\\"shipping_price\\": 5000.0,\\n      \\"method\\": \\"credit\\",\\n      ' \
                          '\\"card\\": {\\n        \\"number\\": \\"344604579207048\\",\\n        ' \
                          '\\"month\\": \\"05\\",\\n        \\"year\\": \\"2021\\",\\n        ' \
                          '\\"cvc\\": 336,\\n        \\"brand\\": \\"American Express\\"\\n      },\\n      ' \
                          '\\"total\\": 5020.0,\\n      \\"status\\": \\"not paid\\",\\n      ' \
                          '\\"message\\": \\"insufficient credit balance\\"\\n    },\\n    ' \
                          '\\"created_at\\": \\"2021-05-18 12:46:44.524000\\",\\n    ' \
                          '\\"updated_at\\": \\"2021-05-18 12:46:44.524690\\"\\n  }\\n]", "log_message": "ok"}'
        mock_requests.return_value = json.loads(expected_result)

        self.assertTrue(get_data_from_order_logs(url=my_url, filter_data=dates)["status"])
