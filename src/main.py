from typing import List

TEST_INPUT_01 = "III"
TEST_INPUT_02 = "LVIII"
TEST_INPUT_03 = "MCMXCIV"
TEST_INPUT_04 = "4"

EXPECTED_OUTPUT_01 = 3
EXPECTED_OUTPUT_02 = 58
EXPECTED_OUTPUT_03 = 1994
EXPECTED_OUTPUT_04 = 0


class LeetCode:
    def run(self, s: str) -> int:
        integer_number = 0


        return integer_number


if __name__ == '__main__':
    test_inputs = [TEST_INPUT_01, TEST_INPUT_02, TEST_INPUT_03, TEST_INPUT_04]
    expected_outputs = [EXPECTED_OUTPUT_01, EXPECTED_OUTPUT_02, EXPECTED_OUTPUT_03, EXPECTED_OUTPUT_04]
    leet_code_tester = LeetCode()

    for i in range(len(test_inputs) - 1):
        print(f'Your Input: {test_inputs[i]} - Expected Output: {expected_outputs[i]}')
        print(f'Your Output: {leet_code_tester.run(test_inputs[i])}')
