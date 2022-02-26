'''
10 15
1 2
2 3
3 4
4 5
5 1
1 6
2 7
3 8
4 9
5 10
6 8
7 9
8 10
9 6
10 7
'''
n, m = map(int, input().split())
like = [{} for _ in range(n + 1)]
child = []
for i in range(m):
    i0, i1 = map(int, input().split())
    like[i0][i], like[i1][i] = 1, 1
    child.append([i0, i1])


vis_c, vis_tang = [0] * m, [0] * (n + 1)
# def check_tang():
#     if sum(vis_tang) < m:
#         r

def bfs(tang):
    index = 0
    while index < len(tang):
        cur = tang[index]
        for c in like[cur].keys():
            if not vis_c[c]:
                next_tang = sum(child[c]) - cur
                if not vis_tang[next_tang]:
                    tang.append(next_tang)
                    vis_tang[next_tang] = 1
                    vis_c[c] = 1
        index += 1

while sum(vis_tang) < n:
    flag = False
    min_child = 100
    start_child = 0
    for i in range(1, n + 1):
        if not vis_tang[i] and (len(like[i].keys()) < min_child):
            min_child = len(like[i].keys())
            # print(i, min_child)
            for c in like[i].keys():
                if not vis_c[c]:
                    start_child = c
                    flag = True
    if not flag:
        break
    # print(start_child)
    vis_c[start_child] =  1
    tang = []
    tangs = [child[start_child][0], child[start_child][1]]
    for t in tangs:
        if not vis_tang[t]:
            vis_tang[t] = 1
            tang.append(t)
    bfs([child[start_child][0], child[start_child][1]])

# print(vis_c, vis_tang)
# print(like)
print(m - sum(vis_c))