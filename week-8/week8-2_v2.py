
n = eval(input())
r = list(map(int, input().split()))
v = list(map(int, input().split()))
import time
start = time.time()
z = list(zip(r, v))
z.sort(key=lambda x:x[1], reverse=True)
sum_r = sum(r)
sum_v = sum(v)
ori_v = z[0][1]
m = 1
while ori_v < sum_r:
    ori_v += z[m][1]
    m += 1
dp = [[-1]*(sum_v + 1) for _ in range(n)]
# print(z)
# for item in dp:
#     print(item)
bucket_cost = 10000
dp[0][0] = 0
for i in range(1, z[0][1] + 1): dp[0][i] = bucket_cost - z[0][0]
for i in range(1, n):
    for j in range(sum_v + 1):
        dp[i][j] = dp[i-1][j]
        left_v = max(j - z[i][1], 0)
        if dp[i-1][left_v] != -1:
            if dp[i][j] != -1:
                dp[i][j] = min(dp[i][j], dp[i-1][left_v] + bucket_cost - z[i][0])
            else:
                dp[i][j] = (dp[i-1][left_v] + bucket_cost - z[i][0])
ans = 10000 * m
for i in range(sum_r, sum_v + 1):
    if dp[n - 1][i] != -1:
        ans = min(ans, dp[n - 1][i])
ans += sum_r - bucket_cost * m
# for item in dp:
#     print(item)
print(m, ans)

# end = time.time()
# print('cost_time =', end-start)
'''
4
3 3 4 3
4 7 6 5

'''