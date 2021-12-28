'''
逆序数
9
1 -1 -1 0 -1 0 1 1 1
'''
n = eval(input())
nums = list(map(abs, (map(int, input().split()))))
for i in range(n):
    nums[i] = [nums[i], i]
# print(nums)
nums.sort()
# print(nums)
ans = 0
for i in range(n-1, -1, -1):
    # print(i)
    pre_num, behind_num = 0, 0
    for j in range(0, i):
        if nums[j][0] < nums[i][0]:
            if nums[j][1] > nums[i][1]:
                behind_num += 1
            else:
                pre_num += 1
    ans += min(pre_num, behind_num)
print(ans)