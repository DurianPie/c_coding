n = eval(input())
desk = [eval(input()) for _ in range(n)]
heights = list(set(desk))
heights.sort()
# print(desk)
# print(heights)
def solve(l, r, height):
    cost_height = r - l
    min_height = min(desk[l:r])
    cost_width =  min_height - height
    pre = l - 1
    for i in range(l, r):
        if desk[i] == min_height:
            if i > pre + 1:
                cost_width += solve(pre + 1, i, min_height)
            pre = i
        elif i == r-1:
            cost_width += solve(pre + 1, r, min_height)
    res = min(cost_height, cost_width)
    return res
res = solve(0, n, 0)
print(res)
'''
7
4
5
2
2
2
1
5
'''