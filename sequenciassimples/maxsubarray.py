'''
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i=0
        j=0
        somas=[]
        while i <= len(nums):
            while j <= len(nums):
                somas.append(sum(nums[i:j]))
                j+=1
            i+=1
            j=i
        return max(somas)

Solution = Solution()
print(Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution.maxSubArray([1]))
print(Solution.maxSubArray([5,4,-1,7,8]))

