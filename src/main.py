import math
from typing import List

TEST_INPUT_01 = [1,5,0,3,5]
TEST_INPUT_02 = [0]
TEST_INPUT_03 = [1,5,0,3,5]
TEST_INPUT_04 = [0]

EXPECTED_OUTPUT_01 = 3
EXPECTED_OUTPUT_02 = 0
EXPECTED_OUTPUT_03 = 3
EXPECTED_OUTPUT_04 = 0


class LeetCode:
    def run(self, nums: List[int]) -> int:
        counter = 0

        while True:
            nums = [num for num in nums if num > 0]

            if not nums:
                break

            min_num = min(nums)
            nums = [num - min_num for num in nums]
            counter += 1

        return counter


if __name__ == '__main__':
    test_inputs = [TEST_INPUT_01, TEST_INPUT_02, TEST_INPUT_03, TEST_INPUT_04]
    expected_outputs = [EXPECTED_OUTPUT_01, EXPECTED_OUTPUT_02, EXPECTED_OUTPUT_03, EXPECTED_OUTPUT_04]
    leet_code_tester = LeetCode()

    for i in range(len(test_inputs)):
        print(f'Your Input: {test_inputs[i]} - Expected Output: {expected_outputs[i]}')
        print(f'Your Output: {leet_code_tester.run(test_inputs[i])}')
