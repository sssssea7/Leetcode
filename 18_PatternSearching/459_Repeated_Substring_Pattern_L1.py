""" https://leetcode.com/problems/repeated-substring-pattern/submissions/
calculate lps and check len(s)%(len(s)-lps[-1])==0
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getLPS(s):
            i = 0
            lps = [0] * len(s)
            for j in range(1, len(s)):
                while s[j] != s[i] and i: i = lps[i-1]
                if s[j] == s[i]: i += 1
                lps[j] = i
            return lps
        
        lps = getLPS(s)
        return lps[-1] and len(s)%(len(s)-lps[-1])==0