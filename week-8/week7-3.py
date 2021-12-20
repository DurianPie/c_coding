# Alice
n, m = map(int, input().split())
ham = [eval(input()) for _ in range(n)]

def check_len(l):
    res = 0
    for i in range(n):
        res += int(ham[i] / l)
    # print(res)
    if res >= m:
        return True
    else:
        return False

def solve(l, r):
    if r - l < 0.001:
        return r
    mid = (l + r) / 2
    if check_len(mid):
        return solve(mid, r)
    else:
        return solve(l, mid)

l = 0
r = max(ham) * 2
# ans = float(int(solve(l, r) * 100))/100
ans = solve(l, r)
print('%.2f' % ans)
print(ans)


'''
5 10
11.16
76.45
98.51
5.79
60.96

'''