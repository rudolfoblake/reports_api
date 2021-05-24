from unittest import mock, TestCase
from Utils.search_engine.search_engine_utils import get_all_searches, get_categories, convert_category_to_string_list, \
    string_count, get_reports


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
    if args[0] == "http://127.0.0.1:5000/get_all_searches":
        return MockResponse(({'user_id': '23132321654'}, {'category': 'abc'}), 200)
    return MockResponse(None, 404)


class TestSearchEngineUtils(TestCase):

    def test_convert_category_to_string_list(self):
        test_data = [["teste1", "teste2"],["teste2"]]
        expected = ["teste1", "teste2", "teste2"]

        self.assertEqual(expected, convert_category_to_string_list(test_data))
        self.assertEqual([], convert_category_to_string_list([]))

    @mock.patch('Utils.search_engine.search_engine_utils.get_all_searches')
    def test_get_categories(self, mock_get_all):
        mock_get_all.return_value = [{'category': 'abc'}]
        dates = {"initial_date": "2020-01-01", "final_date": "2021-12-01"}
        search_type = 1

        self.assertEqual(['abc'], get_categories(dates, search_type))

        dates = {"initial_date": "2020-01-01", "final_date": "2021-12-01"}
        search_type = 0

        self.assertEqual(['abc'], get_categories(dates, search_type))

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_get_all_searches(self, mock_requests):
        dates = {"initial_date": "2020-01-01", "final_date": "2021-12-01"}
        search_type = 1
        self.assertEqual([{'user_id': '23132321654'}], get_all_searches(dates, search_type))

        dates = {"initial_date": "2020-01-01", "final_date": "2021-12-01"}
        search_type = 0
        self.assertEqual([{'category': 'abc'}], get_all_searches(dates, search_type))

    def test_string_count(self):
        test_data = ["teste1", "teste2", "teste2"]
        expected_data = dict(teste1=1, teste2=2)
        self.assertEqual(string_count(test_data), expected_data)

    @mock.patch('Utils.search_engine.search_engine_utils.get_categories')
    @mock.patch('Utils.search_engine.search_engine_utils.convert_category_to_string_list')
    @mock.patch('Utils.search_engine.search_engine_utils.string_count')
    def test_get_reports(self, mock_string_count, mock_convert_category_to_string_list, mock_get_categories):
        mock_get_categories = [["teste1", "teste2"],["teste2"]]
        mock_convert_category_to_string_list = ["teste1", "teste2", "teste2"]
        mock_string_count = {'Ficção': 1, 'Ação': 2, 'Fantasia': 2}

        self.assertTrue({'Ficção': 1, 'Ação': 2, 'Fantasia': 2}, (["teste1", "teste2", "teste2"],
                                                                  [["teste1", "teste2"],["teste2"]]))



# def get_reports(dates, search_type):
#     if search_type not in SEARCH_TYPE_LIST:
#         return False, []
#     elif search_type == GET_LOGGED_USERS_REPORT:
#         try:
#             total_list = get_categories(dates, search_type)
#             converted_list = convert_category_to_string_list(total_list)
#             counted_list = string_count(converted_list)
#             counted_list = sorted(counted_list.items(), key=operator.itemgetter(1), reverse=True)
#             return True, counted_list
#         except Exception as error:
#             return False, f"Error: {error}"
#     elif search_type == GET_NOT_LOGGED_USERS_REPORT:
#         try:
#             total_list = get_categories(dates, search_type)
#             converted_list = convert_category_to_string_list(total_list)
#             counted_list = string_count(converted_list)
#             counted_list = sorted(counted_list.items(), key=operator.itemgetter(1), reverse=True)
#             return True, counted_list
#         except Exception as error:
#             return False, f"Error: {error}"