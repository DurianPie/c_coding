n = int(input())
l = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 0
ans = 0
for i in range(1, n):
    if l[i] > l[i - 1]:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1] + 1
    else:
        dp[i][0] = 1
        if i > 1 and l[i] > l[i - 2]:
            dp[i][1] = dp[i - 2][0] + 1
        elif i < n - 1 and l[i + 1] > l[i - 1]:
            dp[i][1] = dp[i - 1][0]
        else: 
            dp[i][1] = 0
    ans = max(ans, dp[i][0], dp[i][1])
# print(dp)
print(ans)

'''
6
2 3 8 4 5 7

'''