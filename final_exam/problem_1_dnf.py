'''
3
2 4
1 5
3 6
'''
def compare(task_0, task_1):
    unsign = 1
    if task_0[0] > task_1[0]:
        task_0, task_1 = task_1, task_0
        unsign = -1
    if sum(task_0) < sum(task_1):
        return unsign * 1
    elif sum(task_0) > sum(task_1):
        return unsign * -1

n = eval(input())
tasks = [list(map(int, input().split())) for _ in range(n)]
tasks.sort()
# print(n, tasks)
cur_i, cur_t = 0, 0
flag = True
for i in range(n):
    if i < cur_i:
        continue
    task_list = [tasks[i]]
    index = i + 1
    while index < n and tasks[index][1] <= tasks[index - 1] - 1:
        task_list.append(tasks[index])
        index += 1
    task_list.sort()
