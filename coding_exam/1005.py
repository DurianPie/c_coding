n, f, d = map(int, input().split())
like = []
for _ in range(n):
    line = list(map(int, input().split()))
    fn = line[0]
    dn = line[1]
    fi = line[2 : 2 + fn]
    di = line[2 + fn : ]
    like.append([fi, di])
flags = [[0]*(f+1), [0]*(d+1)]
result = 0
def search(ni, maxn):
    global result
    result = max(result, maxn)
    fi, di = like[ni]
    for i in fi:
        if flags[0][i] == 0:
            for j in di:
                if flags[1][j] == 0:
                    if ni == n - 1:
                        result = max(result, maxn + 1)
                    else:
                        flags[0][i] = flags[1][j] = 1
                        search(ni + 1, maxn + 1)
                        flags[0][i] = flags[1][j] = 0
    if ni < n - 1:
        search(ni+1, maxn)
search(0, 0)
print(result)
                   
            

