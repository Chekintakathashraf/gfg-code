"""#Given an array of positive integers arr and a positive integer target, find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If no such subarray exists, return 0."""


def min_subarray_len(target, arr):
    start = 0
    current_sum = 0
    min_length = float('inf')

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    return 0 if min_length == float('inf') else min_length

# Test examples
print(min_subarray_len(7, [2,3,1,2,4,3]))  # 2
print(min_subarray_len(15, [1,2,3,4,5]))   # 5
print(min_subarray_len(100, [1,2,3,4,5]))  # 0 (no subarray)

