from math import *
def CountB(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    m = int(log2(x + 1))
    if 2**m == x + 1:
        return 2**(m-1)
    return x - 2**m + 1 + CountB(2**(m+1) - x - 1)

n = eval(input())
for _ in  range(n):
    l, r = map(int, input().split())
    ans = CountB(r) - CountB(l-1)
    print(ans)
'''
3
1 3
1 7
4 8

'''