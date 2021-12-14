n = eval(input())
val = []
for i in range(n):
    l, r = map(int, input().split())
    val.append([i, l, r])
sorted_l = sorted(val, key=lambda x:x[1], reverse=True)
sorted_r = sorted(val, key=lambda x:x[2], reverse=True)
# print(sorted_l)
# print(sorted_r)
ans, vis = 0, [0] * n
for i in range(n):
    if sorted_l[i][0] == sorted_r[i][0]:
        sorted_r[i], sorted_r[i + 1] = sorted_r[i + 1], sorted_r[i]
    ans += max(sorted_l[i][1], sorted_r[i][2]) + 1
print(ans)
'''
5
5 0
4 2
2 0
5 2
3 0

'''