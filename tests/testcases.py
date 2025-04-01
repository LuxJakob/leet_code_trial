import unittest
from parameterized import parameterized
from src.main import *


class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.instance = LeetCode()

    @parameterized.expand([
        (TEST_INPUT_01, EXPECTED_OUTPUT_01),
        (TEST_INPUT_02, EXPECTED_OUTPUT_02),
        (TEST_INPUT_03, EXPECTED_OUTPUT_03),
        #(TEST_INPUT_04, EXPECTED_OUTPUT_04),
    ])
    def test_run(self, test_input, expected_output):
        result = self.instance.run(test_input)
        self.assertEqual(result, expected_output)
