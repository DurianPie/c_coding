import sys
n = int(input())
nums = map(int, sys.stdin.readline().split(' '))
ans = 0
for num in nums:
    ans ^= num
for i in range(1, n + 1):
    ans ^= i
    
print(ans)