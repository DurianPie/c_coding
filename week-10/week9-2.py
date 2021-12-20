n = int(input())
l = list(map(int, input().split()))

drop_positon = -1
next_drop_positon = -1
ans = 0
for i in range(1, n):
    if l[i] <= l[i - 1]:
        if i < n - 1 and l[i + 1] > l[i - 1]:
            drop_positon = next_drop_positon
            next_drop_positon = i
        elif i == 1 or l[i] > l[i - 2]:
            drop_positon = next_drop_positon
            next_drop_positon = i - 1
        else: drop_positon = next_drop_positon = i
    else:
        if drop_positon == next_drop_positon:
            ans = max(ans, i - drop_positon)
        else:
            ans = max(ans, i - drop_positon - 1)
    # print(drop_positon, next_drop_positon, ans)
print(ans)



'''
6
2 3 8 4 5 7

'''