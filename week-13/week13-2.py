'''
距离产生美
4
0 20 30 50
20 0 50 15
30 50 0 20
50 15 20 0
'''
n = eval(input())
dist = [list(map(int, input().split())) for _ in range(n)]
div = [0] * n

def cal():
    ans = 0
    for i in range(n):
        if div[i] == 0:
            for j in range(n):
                if div[j] == 1:
                    ans += dist[i][j]
    return ans

def dfs(n, i):
    ans = 0
    if i == n-1:
        if sum(div) != 0:
            ans = max(ans, cal())
        if sum(div) != n-1:
            div[i] = 1
            ans = max(ans, cal())
    else:
        ans = max(ans, dfs(n, i+1))
        div[i] = 1
        ans = max(ans, dfs(n, i+1))
        div[i] = 0
    return ans

ans = dfs(n, 0)
print(ans)