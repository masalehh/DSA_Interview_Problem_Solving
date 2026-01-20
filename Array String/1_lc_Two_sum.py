def two_sum(nums, target_sum):
    seen = {}

    for i, num in enumerate(nums):
        complement = target_sum - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
