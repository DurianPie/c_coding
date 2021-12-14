n, m = list(map(int, input().split()))
trace = [[] for _ in range(n)]
people = [[] for _ in range(m)]
for i in range(m):
    record_in = list(map(int, input().split()))
    num = record_in[0]
    record = record_in[1:]
    people[i] = record
    for person in record:
        trace[person].append(i)

visit_n = [0] * n
visit_m = [0] * m
bfs_l = [0]
visit_n[0] = 1
count = 1
while len(bfs_l) != 0:
    sure = bfs_l[0]
    for place in trace[sure]:
        if visit_m[place] == 0:
            visit_m[place] = 1
            for sus in people[place]:
                if visit_n[sus] == 0:
                    bfs_l.append(sus)
                    visit_n[sus] = 1
                    count += 1
    del bfs_l[0]
print(count)
