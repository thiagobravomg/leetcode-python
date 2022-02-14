'''
Given two strings s and t,
return true if t is an anagram of s,
and false otherwise.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lista1 = list(s)
        lista2 = list(t)
        if sorted(lista1) == sorted(lista2):
            return True
        else:
            return False

Solution = Solution()
print(Solution.isAnagram("anagram","nagaram"))
print(Solution.isAnagram("rat","car"))
