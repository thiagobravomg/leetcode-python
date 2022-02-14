'''
Given an integer array nums,
return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i=0
        result=[]
        while i<= len(nums)-1:
            lista=nums[0:len(nums)]
            lista.pop(i)
            result.append(1)
            j=0
            while j<= len(lista)-1:
                result[i]=result[i]*lista[j]
                j+=1
            i+=1
        return result

Solution = Solution()
print(Solution.productExceptSelf([1,2,3,4]))
print(Solution.productExceptSelf([-1,1,0,-3,3]))