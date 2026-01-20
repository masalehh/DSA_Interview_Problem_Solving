def two_sum(nums, target_sum):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target_sum:
                return [i, j]
