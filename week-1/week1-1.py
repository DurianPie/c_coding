import sys
n = eval(input())
string = sys.stdin.readline()
strdict = {}
ans = 1
last = 0
maxlen = 1
for i, item in enumerate(string):
    if item not in strdict or strdict[item] < last:
        if i == 0:
            maxlen = 1
        else:
            maxlen +=  1
        strdict[item] = i
        ans = max(ans, maxlen)
    else:
        last = strdict[item] + 1
        strdict[item] = i
        maxlen = i + 1 - last

print(ans)
