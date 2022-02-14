'''
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        i = 0
        j = 1
        while i <= len(nums) - 2:
            while j <= len(nums) - 1:
                if nums[i] == nums[j]:
                    return True
                else:
                    j = j + 1
            i = i + 1
            j = i + 1
        return False

Solution = Solution()
print(Solution.containsDuplicate([1, 2, 3, 1]))
print(Solution.containsDuplicate([1, 2, 3, 4]))
print(Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
 