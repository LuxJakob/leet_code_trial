import math
from typing import List

TEST_INPUT_01 = 121
TEST_INPUT_02 = -121
TEST_INPUT_03 = 1337
TEST_INPUT_04 = 12121

EXPECTED_OUTPUT_01 = True
EXPECTED_OUTPUT_02 = False
EXPECTED_OUTPUT_03 = False
EXPECTED_OUTPUT_04 = True


class LeetCode:
    def run(self, x: int) -> bool:
        if x < 0:
            return False

        if str(x) == str(x)[::-1]:
            return True

        return False


if __name__ == '__main__':
    test_inputs = [TEST_INPUT_01, TEST_INPUT_02, TEST_INPUT_03, TEST_INPUT_04]
    expected_outputs = [EXPECTED_OUTPUT_01, EXPECTED_OUTPUT_02, EXPECTED_OUTPUT_03, EXPECTED_OUTPUT_04]
    leet_code_tester = LeetCode()

    for i in range(len(test_inputs)):
        print(f'Your Input: {test_inputs[i]} - Expected Output: {expected_outputs[i]}')
        print(f'Your Output: {leet_code_tester.run(test_inputs[i])}')
