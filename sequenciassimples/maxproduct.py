'''
Given an integer array nums,
find a contiguous non-empty subarray within the array that has the largest product,
and return the product.
'''

import math

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        i=0
        j=1
        resultado=[]
        resultado2=[]
        while i <= len(nums)-1:
            while j <= len(nums):
                resultado.append(nums[i:j])
                j+=1
            i+=1
            j=i+1
        for i in resultado:
            resultado2.append(math.prod(i))
        return max(resultado2)

Solution = Solution()
print(Solution.maxProduct([2,3,-2,4]))
print(Solution.maxProduct([-2,0,-1]))


