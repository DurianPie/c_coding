'''
3
14 42 16
13 40 1
17 33 5
'''
import numpy as np
n = eval(input())
t, fin_t, v = [], [], []
for _ in range(n):
    in_t, in_fin_t, in_v = (map(int, input().split()))
    t.append(in_t), fin_t.append(in_fin_t), v.append(in_v)
dp = [[[0]*2000 for _ in range(2000)] for _ in range(n)]
# print(np.array(dp).shape)
last_t = max(fin_t)
ans = 0
for i in range(n):
    for delta_t in range(1, last_t + 1):
        for t1 in range(last_t + 1):
            t2 = t1 + delta_t
            if t2 > last_t:
                break
            if t2 - t[i] >= t1 and t2 <= fin_t[i]:
                dp[i][t1][t2] = max(
                    dp[i-1][t1][t2], 
                    dp[i-1][t1][t2-t[i]] + v[i], 
                    dp[i][t1][t2-1])
            else:
                dp[i][t1][t2] = max(
                    dp[i-1][t1][t2], 
                    dp[i][t1][t2-1])
            # if i == 2:
            print(i, t1, t2, dp[i][t1][t2])
print(dp[n-1][0][last_t])
'''
dp[n][t1][t2]  t1 至 t2 期间， 前n个物品最多价值
dp[n][t1][t2] = max(dp[n-1][t1][t2], dp[n-1][t1][t2-t[n]] + v[n], dp[n][t1][t2-1])

dp[i][t] = max(dp[i-1][t], dp[i-1][t-t[n]])
'''
