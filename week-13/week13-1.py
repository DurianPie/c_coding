'''
小球摆放问题
3 1
...
###
...
'''
n, m = map(int, input().split())
boxs = []
for i in range(n):
    line = input()
    line_binary = [item == '#' for item in line]
    boxs.append(line_binary)
# print(boxs)
visit = [False] * n
ans = 0

def dfs(line_index, remain_m):
    ans = 0
    for i in range(n):
        if boxs[line_index][i] and not visit[i]:
            visit[i] = True
            if remain_m - 1 == 0:
                ans += 1
            elif line_index < n-1:
                ans += dfs(line_index+1, remain_m-1)
            visit[i] = False
    if line_index < n-1:
        ans += dfs(line_index+1, remain_m)
    return ans

ans = dfs(0, m)
print(ans)
