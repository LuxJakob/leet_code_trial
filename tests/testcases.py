import unittest
from parameterized import parameterized
from src.main import LeetCode


class TestMyFunction(unittest.TestCase):

    test_input_01 = 1
    expected_output_01 = 3
    test_input_02 = 1
    expected_output_02 = 4
    test_input_03 = 1
    expected_output_03 = 1

    def setUp(self):
        self.instance = LeetCode()

    @parameterized.expand([
        (test_input_01, expected_output_01),
        (test_input_02, expected_output_02),
        (test_input_03, expected_output_03),
    ])
    def test_run(self, test_input, expected_output):
        result = self.instance.run(test_input)
        self.assertEqual(result, expected_output)
