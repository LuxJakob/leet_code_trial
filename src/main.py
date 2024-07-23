from typing import List


class LeetCode:
    def run(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.reverse()
        appearance_counter = 0
        sorted_nums = []

        while nums:
            appearance_counter += 1
            inner_counter = 0

            for i in range(len(nums)):
                if not nums or inner_counter == len(nums):
                    break

                counter = nums.count(nums[inner_counter])
                if counter == appearance_counter:
                    for j in range(appearance_counter):
                        sorted_nums.append(nums[inner_counter])
                        nums.remove(nums[inner_counter])

                    inner_counter -= 1

                inner_counter += 1

        return sorted_nums


if __name__ == '__main__':
    arguments = (
        [-7, 8, -6, 9, -7, -6, -6, 8, 8]
    )
    leet_code_tester = LeetCode()
    print(f'Your Input: {arguments}')
    print(f'Your Output: {leet_code_tester.run(arguments)}')
