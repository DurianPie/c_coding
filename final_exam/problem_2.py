'''
4
5 6 3
17 22 14
4 8 15
13 2 18
'''
n = eval(input())
huowu = []
for _ in range(n):
    line = list(map(int, input().split()))
    huowu.append(line)
huowu.sort(key=lambda x:x[1])
# print(huowu)
dp = [[0]*2000 for _ in range(n)]
ts, fin_t, v = [], [], []
for i in range(n):
    in_t, in_fin_t, in_v = huowu[i]
    ts.append(in_t), fin_t.append(in_fin_t), v.append(in_v)
# print(np.array(dp).shape)
last_t = fin_t[-1]
# print(last_t)
ans = 0
for i in range(n):
    for t in range(last_t + 1):
        if t <= fin_t[i] and t - ts[i] >= 0:
            dp[i][t] = max(dp[i-1][t], dp[i-1][t-ts[i]] + v[i], dp[i][t-1])
        else:
            dp[i][t] = max(dp[i-1][t], dp[i][t-1])
print(dp[n-1][last_t])
'''
dp[n][t1][t2]  t1 至 t2 期间， 前n个物品最多价值
dp[n][t1][t2] = max(dp[n-1][t1][t2], dp[n-1][t1][t2-t[n]] + v[n], dp[n][t1][t2-1])

dp[i][t] = max(dp[i-1][t], dp[i-1][t-t[n]], d[i][t-1])
'''
