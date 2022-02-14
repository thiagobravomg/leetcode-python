'''
Given an array of strings strs,
group the anagrams together.
You can return the answer in any order.
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        i=0
        k=1
        resultado=[]
        while i <= len(strs)-1:
            listaaux=[strs[i]]
            while k <= len(strs)-1:
                if self.isAnagram(strs[i],strs[k]):
                    listaaux.append(strs[k])
                    strs.pop(k)
                else:
                    k+=1
            resultado.append(listaaux)
            i+=1
            k=i+1
        return resultado

    def isAnagram(self, str1:str, str2:str) -> bool:
        if sorted(str1) == sorted((str2)):
            return True
        else:
            return False

Solution = Solution()
print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams([""]))
print(Solution.groupAnagrams(["a"]))
