"""
def two_sum(nums, target_sum):
    seen = {}

    for i, num in enumerate(nums):
        complement = target_sum - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
"""


def two_sum(nums, target_sum):
    """
    This function finds two numbers in a list that add up to a given target.

    Parameters:
    nums (list): A list of integers.
    target_sum (int): The target value we want to achieve by adding two numbers.

    Returns:
    list: A list containing the indices of the two numbers that add up to target_sum.
          If no such pair exists, the function returns None.
    """

    # Create an empty dictionary to store numbers we have seen so far
    # Key = number from the list
    # Value = index of that number in the list
    seen = {}

    # Loop through the list using enumerate
    # enumerate gives us both index (i) and value (num)
    for i, num in enumerate(nums):

        # Calculate the number needed to reach the target
        # Example: if target is 10 and current num is 3, we need 7
        complement = target_sum - num

        # Check if the complement already exists in the dictionary
        # This means we have already seen the number needed to form the target
        if complement in seen:

            # If found, return the indices:
            # - seen[complement] → index of the previously seen number
            # - i → current index
            return [seen[complement], i]

        # If complement not found, store the current number in the dictionary
        # so it can be used for future comparisons
        seen[num] = i

