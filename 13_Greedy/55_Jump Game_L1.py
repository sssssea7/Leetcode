class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for idx, reach in enumerate(nums):
            if maxJump<idx:
                return False
            maxJump = max(maxJump, idx+reach)
        return True