from unittest import TestCase
from parametrize import parametrize

from lesson_3 import validator_email
from lesson_3.func import isdigit, islower, isalnum
from lesson_3.lists import to_sqr, max_in_half, both_has, to_list


class TestLesson3(TestCase):
    @parametrize(('symbol', 'res'),
                 [('2', False), ('a', True), ('D', True), ('*', False)])
    def test_isdigit(self, symbol, res):
        self.assertEqual(isdigit(symbol), res)

    @parametrize(('symbol', 'res'),
                 [('2', False), ('a', True), ('D', False), ('*', False)])
    def test_islower(self, symbol, res):
        self.assertEqual(islower(symbol), res)

    @parametrize(('symbol', 'res'),
                 [('2', True), ('a', True), ('D', True), ('*', False)])
    def test_isalnum(self, symbol, res):
        self.assertEqual(isalnum(symbol), res)

    @parametrize(('List_num', 'res'),
                 [([2, 5, 8], [4, 25, 64]), ([-2, -5, -8], [4, 25, 64]), ([0], [0])])
    def test_to_sqr(self, List_num, res):
        self.assertEqual(to_sqr(List_num), res)

    @parametrize(('List_num', 'res'),
                 [([2, 5, 8], 8/3), ([-2, -5, -8], -2/3), ([-1, 0], 0)])
    def test_max_in_half(self, List_num, res):
        self.assertEqual(max_in_half(List_num), res)

    @parametrize(('list1', 'list2', 'res'),
                 [([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                   [1, 2, 3, 5, 8, 13]),
                  ([4, 5, 6], [], []),
                  ([1, 2, 3], [4, 5, 6], [])])
    def test_both_has(self, list1, list2, res):
        self.assertEqual(both_has(list1, list2), res)

    def test_to_list__str_given__list_got(self):
        a = 'a'
        b = 'b'
        res = to_list(a, b)
        expected_res = [a, b]
        self.assertEqual(res, expected_res)

    def test_to_list__lists_given__list_got(self):
        a = [1]
        b = [2]
        res = to_list(a, b)
        expected_res = [a, b]
        self.assertEqual(res, expected_res)

    def test_to_list__one_elem_given__list_got(self):
        a = [1]
        res = to_list(a)
        expected_res = [a]
        self.assertEqual(res, expected_res)

    def test_to_list__ten_elem_given__list_got(self):
        res = to_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(res, expected_res)

    def test_is_valid_email__valid_email__True(self):
        email = 'test@biz.com'
        is_valid_email = validator_email.is_valid_email(email)
        self.assertTrue(is_valid_email)

    @parametrize('email',
                 ['', 'testtest.com', 'test @test.com', 'test@ya.ru'])
    def test_is_valid_email__invalid_email__False(self, email):
        is_valid_email = validator_email.is_valid_email(email)
        self.assertFalse(is_valid_email)
