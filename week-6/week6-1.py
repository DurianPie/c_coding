n = eval(input())
A = list(map(int, input().split()))
m = eval(input())
B = list(map(int, input().split()))
A.sort()
B.sort()
i = j = 0
res = 0
while i < n and j < m:
    if abs(A[i] - B[j]) <= 1:
        res +=1
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    else:
        j += 1
print(res)

'''
2
4 2
2
4 4
'''