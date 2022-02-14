'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        lista=list(s)
        i=0
        j=1
        while i <= len(lista) -2:
            if lista[i] == "(":
                if lista[j] == ")":
                   i+=2
                   j+=2
                else:
                    return False
            elif lista[i] == "[":
                if lista[j] == "]":
                    i+=2
                    j+=2
                else:
                    return False
            elif lista[i] == "{":
                if lista[j] == "}":
                    i+=2
                    j+=2
                else:
                    return False
        return True

Solution = Solution()
print(Solution.isValid("()"))
print(Solution.isValid("()[]{}"))
print(Solution.isValid("(]"))