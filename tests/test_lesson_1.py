from unittest import TestCase

from lesson_1.numbers import power


class TestLesson1(TestCase):
    def test_power(self):
        a = 2
        b = 5
        expected_res = 32
        res = power(a, b)
        self.assertEqual(res, expected_res)
