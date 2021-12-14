n = eval(input())
link = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    [i, j] = list(map(int, input().split()))
    link[i].append(j)
    link[j].append(i)
# print(link)
def bfs(link):
    max_depth = 0
    node = [1,2]
    visit = [0] * (n + 1)
    depth = [0] * (n + 1)
    visit[1] = 1
    while len(node) != 0:
        i = node.pop(0)
        for j in link[i]:
            if visit[j] == 0:
                node.append(j)
                depth[j] = depth[i] + 1
                max_depth = max(max_depth, depth[j])
                visit[i] = 1
    return max_depth
max_depth = bfs(link)
ans = 2 * (n - 1) - max_depth
print(ans)
        
'''
4
1 2
1 3
3 4
'''