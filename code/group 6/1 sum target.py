"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""


def two_sum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i

# Test cases
print(two_sum([2,7,11,15], 9))  # Output: [0,1]
print(two_sum([3,2,4], 6))      # Output: [1,2]
print(two_sum([3,3], 6))        # Output: [0,1]
