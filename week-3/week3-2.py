n = eval(input())
tree = [[]]
for i in range(n):
    l, r, v = list(map(int, input().split(' ')))
    tree.append([l, r, v])
# print(tree)
max_v = 0
def find_max_v(BTNode):
    global max_v
    l_v = r_v = 0
    if tree[BTNode][0] != 0:
        l_v = find_max_v(tree[BTNode][0])
    if tree[BTNode][1] != 0:
        r_v = find_max_v(tree[BTNode][1])
    v = max( tree[BTNode][2], tree[BTNode][2] + l_v, 
             tree[BTNode][2] + r_v)
    max_v = max(max_v, v, tree[BTNode][2] + l_v + r_v)
    return v
find_max_v(1)
print(max_v)