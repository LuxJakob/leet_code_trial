from typing import List

TEST_INPUT_01 = "IV"
TEST_INPUT_02 = "LVIII"
TEST_INPUT_03 = "MCMXCIV"
TEST_INPUT_04 = "III"

EXPECTED_OUTPUT_01 = 4
EXPECTED_OUTPUT_02 = 58
EXPECTED_OUTPUT_03 = 1994
EXPECTED_OUTPUT_04 = 3


class LeetCode:
    def run(self, s: str) -> int:
        integer_numbers = []
        integer_number = 0
        temp = 0
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if not s:
            return 0
        for roman in s:
            try:
                roman_number = roman_numbers[roman]
            except:
                return 0

            integer_numbers.append(roman_number)

        for number in integer_numbers:
            if temp == 0:
                integer_numbers_compressed = [number]
                temp += 1
            elif number == integer_numbers[temp - 1]:
                integer_numbers_compressed[-1] += number
                temp += 1
            else:
                integer_numbers_compressed.append(number)
                temp += 1

        integer_numbers_compressed.append(0)
        for count, number in enumerate(integer_numbers_compressed):
            if number == 0:
                break
            elif number > integer_numbers_compressed[count + 1]:
                integer_number += number
            else:
                integer_number -= number

        return integer_number


if __name__ == '__main__':
    test_inputs = [TEST_INPUT_01, TEST_INPUT_02, TEST_INPUT_03, TEST_INPUT_04]
    expected_outputs = [EXPECTED_OUTPUT_01, EXPECTED_OUTPUT_02, EXPECTED_OUTPUT_03, EXPECTED_OUTPUT_04]
    leet_code_tester = LeetCode()

    for i in range(len(test_inputs)):
        print(f'Your Input: {test_inputs[i]} - Expected Output: {expected_outputs[i]}')
        print(f'Your Output: {leet_code_tester.run(test_inputs[i])}')
