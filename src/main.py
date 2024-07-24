from typing import List


class LeetCode:
    def run(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


if __name__ == '__main__':
    argument_01 = (
        [2,7,11,15]
    )
    argument_02 = (
        9
    )
    leet_code_tester = LeetCode()
    print(f'Your Input: {argument_01, argument_02}')
    print(f'Your Output: {leet_code_tester.run(argument_01, argument_02)}')
