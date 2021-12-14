n, m = map(int, input().split())
table = []
tags = [[0] * m for _ in range(n)]
for _ in range(n):
    line = input()
    table.append(line)
def rfs(i, j):
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    l = [[i, j]]

    tags[i][j] = 1
    for [x, y] in l:
        for [dx, dy] in direction:
            xx = x + dx
            yy = y + dy
            if (xx >= 0 and xx < n and
                yy >= 0 and yy < m and
                table[xx][yy] == '#' and
                tags[xx][yy] == 0):
                l.append([xx, yy])
                tags[xx][yy] = 1
            
mines = 0
for i in range(n):
    for j in range(m):
        if (tags[i][j] == 0 and
            table[i][j] == '#'):
            rfs(i, j)
            mines += 1
print(mines)

