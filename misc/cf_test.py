""" https://foobar.withgoogle.com/queue-to-do
"""
def XOR_1_to_n(n):
    m = n%4
    if m==0: return n
    elif m==1: return 1
    elif m==2: return n+1
    else: return 0

def solution(s, l):
    ans = 0
    for i in range(l):
        head = s+(l*(i+1))-i-1
        tail = max(0, s+(l*i)-1)
        ans ^= XOR_1_to_n(head) ^ XOR_1_to_n(tail)
    return ans