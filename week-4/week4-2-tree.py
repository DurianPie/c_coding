n = eval(input())
tags = [[] for _ in range(n)]
for i in range(n):
    tags[i] = (list(map(int, input().split())))
class TreeNode():
    def __init__(self) -> None:
        self.full = 0
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = TreeNode()
    def update(self, index, ql, qr, left, right):
        l_flag = r_flag = False
        if left >= ql and right <= qr:
            index.full = 1
            return True
        else:
            mid = int((left + right) / 2)
            if mid > ql:
                if index.left == None:
                    index.left = TreeNode()
                    l_flag = self.update(index.left, ql, qr, left, mid)
                elif index.left.full == 0:
                    l_flag = self.update(index.left, ql, qr, left, mid)
            if mid < qr:
                if index.right == None:
                    index.right = TreeNode()
                    r_flag = self.update(index.right, ql, qr, mid, right)
                elif index.right.full == 0:
                    r_flag = self.update(index.right, ql, qr, mid, right)
            if (index.left != None and index.right != None and index.left.full == 1 and index.right.full == 1):
                index.full = 1
        return l_flag or r_flag
TreeSize = int(1e7 + 1)
t = Tree()
count = 0
for i in range(n - 1, -1, -1):
    tag = tags[i]
    if t.update(t.root, tag[0], tag[1] + 1, 0, TreeSize + 1):
        count += 1
print(count)

'''
10
3 6
5 7
3 5
2 6
1 9
2 7
0 9
3 6
0 6
2 6
'''