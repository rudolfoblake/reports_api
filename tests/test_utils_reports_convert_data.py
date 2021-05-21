from unittest import TestCase
from Utils.sales.utils_reports_convert_data import convert_lists
from Utils.sales.utils_reports_convert_data import convert_log_data
from Utils.sales.utils_reports_convert_data import transform_list_of_products
from Utils.sales.utils_reports_convert_data import calculate_median_price


class TestUtilsSalesConvertData(TestCase):

    def test_calculate_median_price_work(self):
        self.assertEqual(1.5, calculate_median_price([1, 2]))

    def test_transform_list_of_products_work(self):
        unique_ids = [1, 2]
        list_of_products = [dict(item_id=1,
                                 item_name="banana",
                                 item_quantity=1,
                                 item_price=5.4),
                            dict(item_id=1,
                                 item_name="banana",
                                 item_quantity=1,
                                 item_price=5.4),
                            dict(item_id=2,
                                 item_name="maca",
                                 item_quantity=5,
                                 item_price=6)]

        expected_result = [{'item_id': 1,
                            'item_name': 'banana',
                            'item_quantity': 2,
                            'prices': [5.4, 5.4],
                            'total_price': 10.8},
                           {'item_id': 2,
                            'item_name': 'maca',
                            'item_quantity': 5,
                            'prices': [6],
                            'total_price': 6}]

        self.assertEqual(expected_result, transform_list_of_products(unique_ids, list_of_products))

        self.assertEqual(list, type(transform_list_of_products(unique_ids, list_of_products)))

    def test_convert_log_data_work(self):
        list_of_logs = [{'_id': {'$oid': '60a3f9ef9f5cf6c89b8f22f1'}, 'order': {'products': [{'item_id': '60a3f', 'item_name': 'Harry Potter e a Camara Secreta Volume I', 'item_price': 10, 'item_quantity': 1}, {'item_id': '60a3g', 'item_name': 'Percy Jackson e os Olimpianos', 'item_price': 5, 'item_quantity': 2}, {'item_id': '60a3h', 'item_name': 'Biblia', 'item_price': 5, 'item_quantity': 500}], 'user': {'user_id': {'$oid': '60a3f9ef9f5cf6c89b8f22f1'}, 'address': {'address_state': 'RJ'}}, 'method': 'bill', 'shipping_price': 30.0, 'total': 50.0, 'status': 'waiting bill', 'bill': {'due_date': '2021-05-21', 'documment_date': '2021-05-18', 'value': 50.0, 'barcode': '23700.99999 05182021.143127 36699909765630712916200499955716015823'}, 'message': 'ok'}, 'created_at': '2021-05-18 12:46:44.524000', 'updated_at': '2021-05-18 12:46:44.524690'}, {'_id': {'$oid': '60a3fad49f5cf6c89b8f22f4'}, 'order': {'products': [{'item_id': '60a3f', 'item_name': 'Harry Potter e a Camara Secreta Volume I', 'item_price': 10, 'item_quantity': 1}, {'item_id': '60a3g', 'item_name': 'Percy Jackson e os Olimpianos', 'item_price': 5, 'item_quantity': 2}, {'item_id': '60a3h', 'item_name': 'Biblia', 'item_price': 5, 'item_quantity': 500}], 'user': {'user_id': {'$oid': '60a3fad49f5cf6c89b8f22f4'}, 'address': {'address_state': 'RJ'}}, 'shipping_price': 30.0, 'method': 'credit', 'card': {'number': '344604579207048', 'month': '05', 'year': '2021', 'cvc': 336, 'brand': 'American Express'}, 'total': 50.0, 'status': 'paid', 'message': 'ok'}, 'created_at': '2021-05-18 12:46:44.524000', 'updated_at': '2021-05-18 12:46:44.524690'}, {'_id': {'$oid': '60a3fb079f5cf6c89b8f22f7'}, 'order': {'products': [{'item_id': '60a3f', 'item_name': 'Harry Potter e a Camara Secreta Volume I', 'item_price': 10, 'item_quantity': 1}, {'item_id': '60a3g', 'item_name': 'Percy Jackson e os Olimpianos', 'item_price': 5, 'item_quantity': 2}], 'user': {'user_id': {'$oid': '60a3fb079f5cf6c89b8f22f7'}, 'address': {'address_state': 'AC'}}, 'shipping_price': 5000.0, 'method': 'credit', 'card': {'number': '344604579207048', 'month': '05', 'year': '2021', 'cvc': 336, 'brand': 'American Express'}, 'total': 5020.0, 'status': 'not paid', 'message': 'insufficient credit balance'}, 'created_at': '2021-05-18 12:46:44.524000', 'updated_at': '2021-05-18 12:46:44.524690'}]
        expected_result = [{'item_id': '60a3h',
                            'item_name': 'Biblia',
                            'item_quantity': 1000,
                            'median_price': 5.0,
                            'total_price': 10},
                           {'item_id': '60a3g',
                            'item_name': 'Percy Jackson e os Olimpianos',
                            'item_quantity': 6,
                            'median_price': 5,
                            'total_price': 15},
                           {'item_id': '60a3f',
                            'item_name': 'Harry Potter e a Camara Secreta Volume I',
                            'item_quantity': 3,
                            'median_price': 10,
                            'total_price': 30}]
        self.assertEqual(expected_result, convert_log_data(list_of_logs))

        self.assertEqual(list, type(convert_log_data(list_of_logs)))

    def test_convert_lists_work(self):
        list_of_logs = [{'_id': {'$oid': '60a3f9ef9f5cf6c89b8f22f1'}, 'order': {'products': [{'item_id': '60a3f', 'item_name': 'Harry Potter e a Camara Secreta Volume I', 'item_price': 10, 'item_quantity': 1}, {'item_id': '60a3g', 'item_name': 'Percy Jackson e os Olimpianos', 'item_price': 5, 'item_quantity': 2}, {'item_id': '60a3h', 'item_name': 'Biblia', 'item_price': 5, 'item_quantity': 500}], 'user': {'user_id': {'$oid': '60a3f9ef9f5cf6c89b8f22f1'}, 'address': {'address_state': 'RJ'}}, 'method': 'bill', 'shipping_price': 30.0, 'total': 50.0, 'status': 'waiting bill', 'bill': {'due_date': '2021-05-21', 'documment_date': '2021-05-18', 'value': 50.0, 'barcode': '23700.99999 05182021.143127 36699909765630712916200499955716015823'}, 'message': 'ok'}, 'created_at': '2021-05-18 12:46:44.524000', 'updated_at': '2021-05-18 12:46:44.524690'}, {'_id': {'$oid': '60a3fad49f5cf6c89b8f22f4'}, 'order': {'products': [{'item_id': '60a3f', 'item_name': 'Harry Potter e a Camara Secreta Volume I', 'item_price': 10, 'item_quantity': 1}, {'item_id': '60a3g', 'item_name': 'Percy Jackson e os Olimpianos', 'item_price': 5, 'item_quantity': 2}, {'item_id': '60a3h', 'item_name': 'Biblia', 'item_price': 5, 'item_quantity': 500}], 'user': {'user_id': {'$oid': '60a3fad49f5cf6c89b8f22f4'}, 'address': {'address_state': 'RJ'}}, 'shipping_price': 30.0, 'method': 'credit', 'card': {'number': '344604579207048', 'month': '05', 'year': '2021', 'cvc': 336, 'brand': 'American Express'}, 'total': 50.0, 'status': 'paid', 'message': 'ok'}, 'created_at': '2021-05-18 12:46:44.524000', 'updated_at': '2021-05-18 12:46:44.524690'}, {'_id': {'$oid': '60a3fb079f5cf6c89b8f22f7'}, 'order': {'products': [{'item_id': '60a3f', 'item_name': 'Harry Potter e a Camara Secreta Volume I', 'item_price': 10, 'item_quantity': 1}, {'item_id': '60a3g', 'item_name': 'Percy Jackson e os Olimpianos', 'item_price': 5, 'item_quantity': 2}], 'user': {'user_id': {'$oid': '60a3fb079f5cf6c89b8f22f7'}, 'address': {'address_state': 'AC'}}, 'shipping_price': 5000.0, 'method': 'credit', 'card': {'number': '344604579207048', 'month': '05', 'year': '2021', 'cvc': 336, 'brand': 'American Express'}, 'total': 5020.0, 'status': 'not paid', 'message': 'insufficient credit balance'}, 'created_at': '2021-05-18 12:46:44.524000', 'updated_at': '2021-05-18 12:46:44.524690'}]
        expected_result = ({'60a3f', '60a3h', '60a3g'},
                           [{'item_id': '60a3f',
                             'item_name': 'Harry Potter e a Camara Secreta Volume I',
                             'item_price': 10,
                             'item_quantity': 1},
                            {'item_id': '60a3g',
                             'item_name': 'Percy Jackson e os Olimpianos',
                             'item_price': 5,
                             'item_quantity': 2},
                            {'item_id': '60a3h',
                             'item_name': 'Biblia',
                             'item_price': 5,
                             'item_quantity': 500},
                            {'item_id': '60a3f',
                             'item_name': 'Harry Potter e a Camara Secreta Volume I',
                             'item_price': 10,
                             'item_quantity': 1},
                            {'item_id': '60a3g',
                             'item_name': 'Percy Jackson e os Olimpianos',
                             'item_price': 5,
                             'item_quantity': 2},
                            {'item_id': '60a3h',
                             'item_name': 'Biblia',
                             'item_price': 5,
                             'item_quantity': 500},
                            {'item_id': '60a3f',
                             'item_name': 'Harry Potter e a Camara Secreta Volume I',
                             'item_price': 10,
                             'item_quantity': 1},
                            {'item_id': '60a3g',
                             'item_name': 'Percy Jackson e os Olimpianos',
                             'item_price': 5,
                             'item_quantity': 2}])
        self.assertEqual(expected_result, convert_lists(list_of_logs))

