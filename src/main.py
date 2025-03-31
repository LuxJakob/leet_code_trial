from typing import List


class LeetCode:
    def run(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        i = 0

        strs.sort()
        for letter in strs[0]:
            current_letter = letter
            for word in strs:
                if current_letter != word[i]:
                    return prefix
            prefix = prefix + current_letter
            i = i + 1

        return prefix  # No solution found


if __name__ == '__main__':
    argument_01 = (
        ["flower", "flower"]
    )
    argument_02 = (
        ["dog","racecar","car"]
    )
    leet_code_tester = LeetCode()
    print(f'Your Input: {argument_02}')
    print(f'Your Output: {leet_code_tester.run(argument_02)}')
