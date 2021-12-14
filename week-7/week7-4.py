from math import *
Pi = acos(-1.0)
n, m = map(int, input().split())
r = [eval(input()) for _ in range(n)]
def check_r2(r2):
    res = 0
    for i in range(n):
        res += int((r[i] ** 2) / r2)
        # print(res)
    if res > m:
        return True
    else:
        return False

def solve(l_r2, r_r2):
    if r_r2 - l_r2 < 0.00001:
        return r_r2
    mid = (l_r2 + r_r2) / 2
    if check_r2((mid)):
        return solve(mid, r_r2)
    else:
        return solve(l_r2, mid)

l_r2 = 0
r_r2 = (max(r) ** 2 * 2)
# ans = float(int(solve(l, r) * 100))/100
ans = solve(l_r2, r_r2) * Pi
print('%.4f' % ans)
# print(ans)



'''
7 9
25
13
14
13
3
27
9

'''