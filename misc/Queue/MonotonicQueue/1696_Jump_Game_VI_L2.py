""" https://leetcode.com/problems/jump-game-vi/
TODO: https://leetcode.com/problems/jump-game-vi/discuss/1260696/Python-Monotonic-deque-explained
"""
class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        dq = deque([(0, A[0])])
        ans = A[0]
        for i in range(1, len(A)):
            while dq and i-dq[0][0]>k: dq.popleft()
            A[i] += dq[0][1]
            while dq and dq[-1][1]<A[i]: dq.pop()
            dq.append((i, A[i]))
        return A[-1]