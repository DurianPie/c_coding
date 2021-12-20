from math import *
# import matplotlib.pyplot as plt
# import numpy as np

class point():
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

def dis(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

class line():
    def __init__(self, p1=point(0,0), p2=point(0,0)) -> None:
        self.p1 = p1
        self.p2 = p2
        self.a = p1.y - p2.y
        self.b = p2.x - p1.x
        self.c = p1.x * p2.y - p2.x * p1.y

def Equal_divide_line(p1, p2):
    mid_p = point((p1.x + p2.x)/2, (p1.y + p2.y)/2)
    tem_line = line(p1, p2)
    p_2 = point(mid_p.x + tem_line.a, mid_p.y + tem_line.b)
    return line(mid_p, p_2)

def GetCrossPoint(line1, line2):
    D = line1.a * line2.b - line2.a * line1.b
    if D == 0:
        return point(0, 0)
    else:
        x = (line1.b * line2.c - line2.b * line1.c) / D
        y = (line2.a * line1.c - line1.a * line2.c) / D
        return point(x, y)

def Find_wifi(p):
    global wifis
    min_dis = 9999999
    result = 0
    for i, wifi in enumerate(wifis):
        if dis(wifi, p) < min_dis:
            result = i
            min_dis = dis(wifi, p)
    return result

def solve(p1, p2):
    # paint_line(l, min(p1.x, p2.x), max(p1.x, p2.x))

    wifi1 = Find_wifi(p1)
    wifi2 = Find_wifi(p2)
    if wifi1 == wifi2:
        return 0
    else:
        divide_line = Equal_divide_line(wifis[wifi1], wifis[wifi2])
        # paint_line(divide_line)
        mid_point = GetCrossPoint(divide_line, line(p1, p2))
        wifimid = Find_wifi(mid_point)
        # paint_point(wifis[wifi1])
        # paint_point(wifis[wifi2])
        # paint_point(wifis[wifimid])
        # print(wifi1, wifi2, wifimid, '\t', p1.x, p1.y, p2.x, p2.y, mid_point.x, mid_point.y)
        if wifimid == wifi1 or wifimid == wifi2:
            return 1
        return solve(p1, mid_point) + solve(mid_point, p2)

# def paint_line(l, left=0, right=1000):
#     x = np.arange(left, right, 1)
#     y = - (l.a * x + l.c) / l.b
#     plt.plot(x, y)   

# def paint_point(p):
#     plt.scatter(p.x, p.y)


n, m = map(int, input().split())
points = [[0, 0], ]
wifis = []
paths = []
paint_x = paint_y = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(point(x, y))
# paint_x = np.array(paint_x)
# paint_y = np.array(paint_y)

for _ in range(m):
    x, y = map(int, input().split())
    paint_x.append(x)
    paint_y.append(y)
    wifis.append(point(x, y))
    # plt.scatter(x, y)
# plt.scatter(paint_x, paint_y)


k = eval(input())
for _ in range(k):
    s, e = map(int, input().split())
    paths.append([s, e])

for i in range(k):
    res = solve(points[paths[i][0]], points[paths[i][1]])
    print(res)

# plt.axis('equal')
# plt.show()

'''
4 4
0 2
1 3
1 0
2 0
1 2
1 1
2 2
2 1
4
1 2
1 3
1 4
3 4

'''