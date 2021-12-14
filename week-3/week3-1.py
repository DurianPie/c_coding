n = eval(input())
PreOrder = list(map(int, input().split()))
MidOrder = list(map(int, input().split()))
tree = [[0] * 2 for _ in range(n + 1)]
root = PreOrder[0]
def build(Pre_Order, Mid_Order):
    if(len(Pre_Order) == 0):
        return 0
    r = Pre_Order[0]
    for i, item in enumerate(Mid_Order):
        if item == r:
            tree[r][0] = build(Pre_Order[1: i + 1], Mid_Order[:i])
            # if i + 1 < len(Mid_Order):
            tree[r][1] = build(Pre_Order[i + 1:], Mid_Order[i + 1:])
    return r
build(PreOrder, MidOrder)
# print (tree)
def postOrder(tree, root):
    if tree[root][0] != 0:
        postOrder(tree, tree[root][0])
    if tree[root][1] != 0:
        postOrder(tree, tree[root][1])
    print(root, end=' ')
postOrder(tree, root)