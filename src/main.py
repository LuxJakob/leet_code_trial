import math
from typing import List

TEST_INPUT_01 = [1,2,3]
TEST_INPUT_02 = [4,3,2,1]
TEST_INPUT_03 = [9]
TEST_INPUT_04 = [0]

EXPECTED_OUTPUT_01 = [1,2,4]
EXPECTED_OUTPUT_02 = [4,3,2,2]
EXPECTED_OUTPUT_03 = [1,0]
EXPECTED_OUTPUT_04 = [1]


class LeetCode:
    def run(self, digits: List[int]) -> List[int]:
        output_str = ""
        digits_plus = []
        for num in digits:
            output_str += str(num)
        output_int  = int(output_str)
        output_int += 1
        output_str = str(output_int)
        for num in output_str:
            digits_plus.append(int(num))
        return digits_plus


if __name__ == '__main__':
    test_inputs = [TEST_INPUT_01, TEST_INPUT_02, TEST_INPUT_03, TEST_INPUT_04]
    expected_outputs = [EXPECTED_OUTPUT_01, EXPECTED_OUTPUT_02, EXPECTED_OUTPUT_03, EXPECTED_OUTPUT_04]
    leet_code_tester = LeetCode()

    for i in range(len(test_inputs)):
        print(f'Your Input: {test_inputs[i]} - Expected Output: {expected_outputs[i]}')
        print(f'Your Output: {leet_code_tester.run(test_inputs[i])}')
