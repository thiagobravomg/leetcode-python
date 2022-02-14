'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function,
nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i=0
        j=len(nums)-1
        middle=i+((i+j)//2)
        snums=sorted(nums[:])
        if j <= 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        elif snums[i]==target:
            return nums.index(snums[i])
        elif snums[j]==target:
            return nums.index(snums[j])
        while j != i + 2:
            if snums[middle] == target:
                return middle
            elif snums[middle] > target:
                j=middle
                middle = i + ((i + j) // 2)
            elif snums[middle] < target:
                i=middle
                middle = i + ((i + j) // 2)
        if snums[i+1] == target:
            return nums.index(snums[i])
        else:
            return -1

Solution = Solution()
print(Solution.search([4,5,6,7,0,1,2],0))
print(Solution.search([4,5,6,7,0,1,2],3))
print(Solution.search([1],0))