'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = 1
        while i <= len(nums) - 2:
            while j <= len(nums) - 1:
                if nums[i] + nums[j] == target:
                    twosum = [i, j]
                    return twosum
                else:
                    j = j + 1
            i = i + 1
            j = i + 1


Solution = Solution()
print(Solution.twoSum([2, 7, 11, 15], 9))
print(Solution.twoSum([3, 2, 4], 6))
print(Solution.twoSum([3, 3], 6))