from unittest import TestCase

from lesson_4.dict import cube_dict, sum_dict_values, max_min_dict, dict_union, mutiply_dict_values, count_letters, \
    dict_from_list


class TestLesson4(TestCase):
    def test_cube_dict(self):
        num = 3
        res = cube_dict(num)
        expected_res = {1: 1, 2: 8, 3: 27}
        self.assertEqual(res, expected_res)

    def test_sum_dict_values(self):
        my_dict = {'data1': 100, 'data2': -100, 'data3': 0}
        res = sum_dict_values(my_dict)
        expected_res = 100 - 100 + 0
        self.assertEqual(res, expected_res)

    def test_max_min_dict(self):
        my_dict = {1: 100, 2: -100, 3: 0}
        res = max_min_dict(my_dict)
        expected_res = [100, -100]
        self.assertEqual(res, expected_res)

    def test_dict_union(self):
        dictionary_1 = {'a': 100, 'b': 200}
        dictionary_2 = {'c': 300, 'd': 400}
        res = dict_union(dictionary_1, dictionary_2)
        expected_res = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
        self.assertEqual(res, expected_res)

    def test_mutiply_dict_values(self):
        my_dict = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
        res = mutiply_dict_values(my_dict)
        expected_res = 375 * 567 * (-37) * 21
        self.assertEqual(res, expected_res)

    def test_count_letters(self):
        string = 'pythonist'
        res = count_letters(string)
        expected_res = {'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'i': 1, 's': 1}
        self.assertEqual(res, expected_res)

    def test_dict_from_list(self):
        my_list = [1, 2, 3, 4, 4, 1, 3, 4, 5, 5, 5, 5]
        res = dict_from_list(my_list)
        expected_res = {1: 2, 2: 1, 3: 2, 4: 3, 5: 4}
        self.assertEqual(res, expected_res)
