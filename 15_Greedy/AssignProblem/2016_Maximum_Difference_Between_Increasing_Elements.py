""" L1: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
greedily find the minimum left element and current maximum difference between right element and left element.
"""
class Solution:
    def maximumDifference(self, A: List[int]) -> int:
        ans = -1
        l = float('inf')
        for r in A:
            if r>l: ans = max(ans, r-l)
            l = min(r, l)
        return ans

class Solution:
    def maximumDifference(self, A: List[int]) -> int:
        ans = -1
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[j]>A[i]: ans = max(ans, A[j]-A[i])
        return ans 