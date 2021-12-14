reward_str, n = input().split()
n = eval(n)
graph = [[] for _ in range(n + len(reward_str) + 2)]
for i in range(1, n+1):
    roll = input().split()
    graph[0].append([i, 1])
    dic = {}
    for l in roll:
        if l not in dic:
            dic[l] = 1
        else:
            continue
        for j in range(len(reward_str)):
            if l == reward_str[j]:
                graph[i].append([n + j + 1, 1])
for i in range(len(reward_str)):
    graph[n + i + 1].append([n + len(reward_str) + 1, 1])
# print((graph))
def dfs(node):
    vis[node] = 1
    global graph
    flag = False
    if node == n + len(reward_str) + 1:
        return True
    for i, edge in enumerate(graph[node]):
        # print(i, edge[0])
        if vis[edge[0]] != 0:
            continue
        if dfs(edge[0]):
            flag = True
            graph[edge[0]].append([node, 1])
            del graph[node][i]
            break
    return flag
count = 0
vis = [0] * (n + len(reward_str) + 2)
while dfs(0):
    count += 1
    vis = [0] * (n + len(reward_str) + 2)
    # print(count)
    # print(graph)
if count == len(reward_str):
    print(1)
else:
    print(0)
'''
q22 3
f m 8 6 2 a
n 9 4 1 2 2
5 y 6 b d q
'''