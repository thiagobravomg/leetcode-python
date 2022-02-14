'''
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<3:
            vazia=[]
            return vazia
        else:
            i=0
            j=0
            k=0
            result=[]
            while i <= len(nums)-1:
                j=0
                while j <= len(nums) - 1:
                    k=0
                    while k <= len(nums) - 1:
                        if sum([nums[i],nums[j],nums[k]])==0 and i!=j and i!=k and j!=k:
                            count=0
                            z=0
                            while z <= len(result)-1:
                                if sorted(result[z]) == sorted([nums[i],nums[j],nums[k]]):
                                    count+=1
                                z+=1
                            if count==0:
                                result.append([nums[i],nums[j],nums[k]])
                            else:
                                count=0
                        k+=1
                    j+=1
                i+=1
        return result
Solution = Solution()
print(Solution.threeSum([-1,0,1,2,-1,-4]))
print(Solution.threeSum([]))
print(Solution.threeSum([0]))