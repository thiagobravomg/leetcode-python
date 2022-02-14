'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        j = 1
        lucros=[]
        while i <= len(prices) - 2:
            while j <= len(prices) - 1:
                lucros.append(prices[j] - prices[i])
                j = j + 1
            i = i + 1
            j = i + 1
        if max(lucros)>=0:
            return max(lucros)
        else:
            return 0
Solution = Solution()
print(Solution.maxProfit([7,1,5,3,6,4]))
print(Solution.maxProfit([7,6,4,3,1]))