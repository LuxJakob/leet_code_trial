import unittest
from parameterized import parameterized
from src.main import LeetCode


class TestMyFunction(unittest.TestCase):

    test_input_01 = ["flower","flow","flight"]
    expected_output_01 = "fl"
    test_input_02 = ["dog","racecar","car"]
    expected_output_02 = ""
    test_input_03 = [-1,1,-6,4,5,-6,1,4,1]
    expected_output_03 = [5,-1,4,4,-6,-6,1,1,1]
    test_input_04 = [1,5,0,5]
    expected_output_04 = [1,0,5,5]

    def setUp(self):
        self.instance = LeetCode()

    @parameterized.expand([
        (test_input_01, expected_output_01),
        (test_input_02, expected_output_02),
        #(test_input_03, expected_output_03),
        #(test_input_04, expected_output_04),
    ])
    def test_run(self, test_input, expected_output):
        result = self.instance.run(test_input)
        self.assertEqual(result, expected_output)
