""" Google
conditional judgement to build a list:
`A[i] = [1 if n == 0 else 0 for n in A[i]]`
"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = A[i][::-1]
            A[i] = [1 if n == 0 else 0 for n in A[i]]
        return A