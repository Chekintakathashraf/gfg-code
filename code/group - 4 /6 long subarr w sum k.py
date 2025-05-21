"""Given an array of integers nums and an integer k, return the length of the longest subarray whose sum equals exactly k."""


def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_len = 0
    seen = {}  # Stores prefix_sum : first_index
    seen[0] = -1  # Edge case: sum from index 0

    for i, num in enumerate(nums):
        prefix_sum += num
        if (prefix_sum - k) in seen:
            length = i - seen[prefix_sum - k]
            max_len = max(max_len, length)
        if prefix_sum not in seen:
            seen[prefix_sum] = i  # Only store first occurrence
    return max_len

# Test cases
print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))  # Output: 4
print(longest_subarray_sum_k([-2, -1, 2, 1], 1))     # Output: 2
print(longest_subarray_sum_k([1, 2, 3], 3))          # Output: 2
