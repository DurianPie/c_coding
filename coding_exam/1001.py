n = int(input())
while n != 0:
    nums = list(map(int, input().split()))
    maxsum = max(nums)
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
        maxsum = max(nums[i], maxsum)
    print(maxsum)
    n = int(input())