n = eval(input())
tags = [[] for _ in range(n)]
for i in range(n):
    tags[i] = (list(map(int, input().split())))
# print(tags)
class TreeNode():
    def __init__(self) -> None:
        self.full = 0
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n * 4)
    def update(self, index, ql, qr, left, right):
        l_flag = r_flag = False
        if left >= ql and right <= qr:
            self.tree[index] = 1
            # print(index, left, right, 'full')
            return True
        else:
            mid = int((left + right) / 2)
            if mid > ql and self.tree[index * 2] == 0:
                l_flag = self.update(index * 2, ql, qr, left, mid)
            if mid < qr and self.tree[index * 2 + 1] == 0:
                r_flag = self.update(index * 2 + 1, ql, qr, mid, right)
            if (self.tree[index * 2] == 1 and self.tree[index * 2 + 1] ==1):
                self.tree[index] = 1
                # print(index, left, right, 'full')
        return l_flag or r_flag
TreeSize = int(1e7 + 1)
t = Tree(TreeSize)
count = 0
for i in range(n - 1, -1, -1):
    tag = tags[i]
    # print(i, tag)
    if t.update(1, tag[0], tag[1] + 1, 0, TreeSize + 1):
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