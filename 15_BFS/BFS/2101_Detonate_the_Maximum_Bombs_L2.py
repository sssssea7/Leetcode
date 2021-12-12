""" https://leetcode.com/problems/detonate-the-maximum-bombs/
the most difficult part is to convert the geometry problem to graph problem
"""
class Solution:
    def maximumDetonation(self, A: List[List[int]]) -> int:
        G = defaultdict(list)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                xi, yi, ri = A[i]
                xj, yj, rj = A[j]
                dist = (xi-xj)**2+(yi-yj)**2
                if dist<=ri**2: G[i].append(j)
                if dist<=rj**2: G[j].append(i)
            
        def bfs(node):
            stk = [node]
            while stk:
                i = stk.pop()
                for j in G[i]:
                    if j not in seen:
                        seen.add(j)
                        stk.append(j)
            return len(seen)
        
        ans = 0
        for i in range(len(A)):
            seen = set([i])
            bfs(i)
            ans = max(ans, len(seen))
        return ans