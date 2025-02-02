""" https://leetcode.com/problems/queue-reconstruction-by-height/
greedy by sorting and inserting
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1])) #tallest -> shortest
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans 