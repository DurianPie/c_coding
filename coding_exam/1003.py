n = int(input())
string = input()
maxstring = [[0, 1] for _ in range(n)]
result = 1
for i in range(n):
    for m in maxstring[i - 1]:
        if (i - m - 1 >= 0 and 
            string[i - m - 1] == string[i]):
            maxstring[i].append(m+2)
            result = max(result, m+2)
print(result)


