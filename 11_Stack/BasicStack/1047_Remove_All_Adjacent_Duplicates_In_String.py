""" L0
pop stack if last stack element equals to current
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        for i, c in enumerate(S):
            if stk and stk[-1]==c: stk.pop()
            else: stk.append(c)
        return "".join(stk)