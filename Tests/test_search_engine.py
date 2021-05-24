from unittest import mock, TestCase
from Utils.search_engine import search_engine_utils


class TestSearchEngineUtils(TestCase):

    def test_convert_category_to_string_list(self):
        test_data = [["teste1", "teste2"],["teste2"]]
        expected = ["teste1", "teste2", "teste2"]
        self.assertEqual(search_engine_utils.convert_category_to_string_list(test_data), expected)

    def test_string_count(self):
        test_data = ["teste1", "teste2", "teste2"]
        expected_data = dict(teste1=1, teste2=2)
        self.assertEqual(search_engine_utils.string_count(test_data), expected_data)

    # @mock.patch("Utils.search_engine.search_engine_utils.string_count", create=True)
    # @mock.patch("Utils.search_engine.search_engine_utils.convert_category_to_string_list", create=True)
    # @mock.patch("Utils.search_engine.search_engine_utils.get_categories_of_logged_users", create=True)
    # def test_get_logged_users_report(self, mock_get_categories_of_logged_users,
    #                                  mock_convert_category_to_string_list,
    #                                  mock_string_count):
    #     mock_get_categories_of_logged_users.return_value = []
    #     mock_convert_category_to_string_list.return_value = []
    #     mock_string_count.return_value = dict()
    #     self.assertEqual(search_engine_utils.get_logged_users_report(dict()), [])






