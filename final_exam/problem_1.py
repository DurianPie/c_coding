'''
3
2 4
1 5
3 6
'''
offset = 1e-6
n = eval(input())
tasks = [list(map(int, input().split())) for _ in range(n)]
tasks.sort(key=lambda x:sum(x))
# print(n, tasks)
cur_t = 0
flag = True
for i in range(n):
    if cur_t > sum(tasks[i]) / 2:
        flag = False
        break
    elif tasks[i][0] >= cur_t:
        cur_t = sum(tasks[i]) / 2 + offset
    else:
        cur_t += (tasks[i][1] - tasks[i][0]) / 2 + offset
    # print(cur_t)
if flag:
    print(1)
else:
    print(0)