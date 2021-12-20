n = eval(input())
line_1 = list(map(int, input().split()))
line_2 = list(map(int, input().split()))
dp = [[0]*2 for _ in range(n)]
ans = 0
max_0 = dp[0][0] = line_1[0]
max_1 = dp[0][1] = line_2[0]
for i in range(1, n):
    dp[i][0] = max_1 + line_1[i]
    dp[i][1] = max_0 + line_2[i]
    max_0 = max(max_0, dp[i][0])
    max_1 = max(max_1, dp[i][1])
    ans = max(ans, dp[i][0], dp[i][1])
print(ans)

'''
3
1 2 9
10 1 1

'''