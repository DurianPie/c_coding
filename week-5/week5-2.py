[n, m, s, t] = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    [i, j] = list(map(int, input().split()))
    graph[i].append(j)
# print(graph)
def bfs():
    visit = [0] * (n + 1)
    l = [s]
    visit[s] = 1
    while(len(l) != 0):
        node = l.pop(0)
        # print(node)
        for j in graph[node]:
            if j == t:
                return True
            elif visit[j] == 0:
                visit[j] = 1
                l.append(j)
    return False
if bfs():
    print(1)
else:
    print(0)
"""
5 7 2 5
1 3
3 2
1 4
1 5
2 1
4 3
4 2
"""