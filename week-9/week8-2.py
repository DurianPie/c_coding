infile = '1002(1)/1.in'
f = open(infile, 'r')
n = eval(f.readline().strip('\n'))
r = list(map(int, f.readline().strip('\n').split()))
v = list(map(int, f.readline().strip('\n').split()))
import time
# n = eval(input())
# r = list(map(int, input().split()))
# v = list(map(int, input().split()))
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
dp = [[[-1]*(ori_v + 1) for _ in range(m + 1)] for _ in range(n)]
# print(dp)
dp[0][0][0] = 0
for i in range(z[0][1] + 1): dp[0][1][i] = z[0][0]
for i in range(1, n):
    dp[i][0][0] = 0
    for j in range(1, min(m + 1, i + 2)):
        for k in range(ori_v + 1):
            dp[i][j][k] = dp[i-1][j][k]
            left_v = max(k-z[i][1], 0)
            if dp[i-1][j-1][left_v] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][left_v] + z[i][0])
            if dp[i][j][k] == -1:
                break
ans = 0
for k in range(sum_r, ori_v + 1):
    ans = max(ans, dp[n-1][m][k])
ans = sum_r - ans
# print(dp)
print(m, ans)

end = time.time()
print('cost_time =', end-start)
'''
4
3 3 4 3
4 7 6 5

'''