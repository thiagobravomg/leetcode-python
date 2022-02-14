'''
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        resultado=intervals[0:len(intervals)]
        while True:
            i = 0
            j = 1
            x=len(resultado)
            while i <= len(resultado) - 2:
                while j <= len(resultado) - 1:
                    if self.result(resultado[i], resultado[j]) != False:
                        resultado.append(self.result(resultado[i], resultado[j]))
                        resultado.pop(i)
                        resultado.pop(j-1)
                    j += 1
                i+=1
                j=i+1
            y = len(resultado)
            if y<x:
                continue
            else:
                break
        return resultado

    def result(self, int1:list[int],int2:list[int]) -> list[int]:
        if int1[0]<int2[0] and int1[1]>int2[1]:
            return int1
        elif int1[0]<int2[0] and int1[1]>=int2[0] and int1[1]<int2[1]:
            return [int1[0],int2[1]]
        elif int1[0]>int2[0] and int1[1]<int2[1]:
            return int2
        elif int1[0]>int2[0] and int1[1]>=int2[1] and int1[0]<int2[1]:
            return [int2[0],int1[1]]
        else:
            return False

Solution = Solution()
print(Solution.merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution.merge([[1,4],[4,5]]))
