""" https://leetcode.com/problems/top-k-frequent-elements/
"""
class Solution:
    def topKFrequent(self, A: List[int], k: int) -> List[int]:
        cnt = Counter(A)
        bucket = [[] for _ in A]
        
        for x, v in cnt.items():
            bucket[-v].append(x)
        
        ans = []
        for x in bucket:
            if len(ans)<k: ans.extend(x)
        else: return ans