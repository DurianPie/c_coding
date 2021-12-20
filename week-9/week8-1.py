# infile = '1001(1)/2.in'
# f = open(infile, 'r')
# n = eval(f.readline().strip('\n'))
# cost = list(map(int, f.readline().strip('\n').split()))
# strs = []
# if len(cost) > n:
#     strs = [str(cost[n])]
#     strs_new = [f.readline().strip('\n') for _ in range(n-1)]
# else:
#     strs_new = [f.readline().strip('\n') for _ in range(n)]
# strs += strs_new
n = eval(input())
cost = list(map(int, input().split()))
strs = []
if len(cost) > n:
    strs = [str(cost[n])]
    strs_new = [input() for _ in range(n - 1)]
else:
    strs_new = [input() for _ in range(n)]
strs += strs_new
reversed_strs = [''.join(reversed(s)) for s in strs]
dp = [[-1, -1] for _ in range(n)]
dp[0] = [0, cost[0]]
for i in range(1, n):

    if strs[i] >= strs[i - 1] and dp[i-1][0] != -1:
        dp[i][0] = dp[i-1][0]
    if strs[i] >= reversed_strs[i-1] and dp[i-1][1] != -1:
        if dp[i][0] == -1:
            dp[i][0] = dp[i-1][1]
        else:
            dp[i][0] = min(dp[i][0], dp[i-1][1])
    if reversed_strs[i] >= strs[i - 1] and dp[i-1][0] != -1:
        dp[i][1] = dp[i-1][0] + cost[i]
    if reversed_strs[i] >= reversed_strs[i-1] and dp[i-1][1] != -1:
        if dp[i][1] == -1:
            dp[i][1] = dp[i-1][1] + cost[i]
        else:
            dp[i][1] = min(dp[i][1], dp[i-1][1] + cost[i])
ans = min(dp[n-1][0], dp[n-1][1])
if ans == -1:
    ans = max(dp[n-1][0], dp[n-1][1])
print(ans)
# print(dp)
'''
4
0 0 8 6 7
bi
qp
bt

'''