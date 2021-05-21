from unittest import mock, TestCase
import requests
from Utils.products import products_utils
from unittest.mock import Mock


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "http://localhost:5000/books":
        return MockResponse(dict(result_data=[dict(item_quantity=0), dict(item_quantity=1)]), 200)
    return MockResponse(None, 404)


class TestProductsUtils(TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_products_with_empty_stock_works(self, mock_requests):
        self.assertEqual(products_utils.get_all_products_with_empty_stock(), [dict(item_quantity=0)])

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_products_works(self, mock_requests):
        self.assertEqual(products_utils.get_all_products(),
                         dict(result_data=[dict(item_quantity=0), dict(item_quantity=1)]))

    def test_calculate_profit_by_product_works(self):
        data_values = dict(result_data=[dict(item_price=100, item_cost_price=50)])
        self.assertEqual(products_utils.calculate_profit_by_product(data_values),
                         [dict(item_price=100, item_cost_price=50, profit_margin="100.0%")])
