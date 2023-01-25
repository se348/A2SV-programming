def lessOrEqual(nums, k):
    nums.sort()
    if k == -1:
        if nums[0] == 1:
            return -1
        return nums[0] -1
    val = nums[k]

    if k == len(nums) -1:
        return val

    if nums[k+1] == val:
        return -1

    return val

length, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(lessOrEqual(arr, k-1))
