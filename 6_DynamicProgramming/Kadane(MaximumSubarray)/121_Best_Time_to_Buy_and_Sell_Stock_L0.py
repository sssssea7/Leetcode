""" L0: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
minimize buy and maximize profit&loss
"""
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        ans = cur = 0
        for i in range(1, len(A)):
            cur = max(0, cur+A[i]-A[i-1])
            ans = max(ans, cur)
        return ans
    
# dp solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        dp = [0] * len(prices)
        dp[0] = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(prices[i]-min_p, dp[i-1])
            min_p = min(prices[i], min_p)
        return dp[-1]