n, r = map(int, input().split())
value = list(map(int, input().split()))
cost = list(map(int, input().split()))
# dp = [[0]*(r + 1) for _ in range(n)]
dp = [0] * (r+1) 
dp_1 = [0] * (r+1) 
for i in range(cost[0], r + 1): dp[i] = value[0]
for i in range(1, n):
    for j in range(r + 1):
        dp_1[j] = dp[j]
        if j - cost[i] >= 0:
            dp_1[j] = max(dp[j], dp[j - cost[i]] + value[i])
    dp, dp_1 = dp_1, dp
ans = dp[r]
# print(dp)
print(ans)

'''
5 14
8 2 2 2 8
7 8 4 5 3

'''