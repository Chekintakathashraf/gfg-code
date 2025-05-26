def longest_subarray_sum_k(arr, k):
    prefix_map = {0: -1}
    curr_sum = 0
    max_len = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum - k in prefix_map:
            length = i - prefix_map[curr_sum - k]
            max_len = max(max_len, length)

        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i

    return max_len


print(longest_subarray_sum_k([1, 2, 3, 1, 1, 1, 1], 5))  # Output: 3
print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))      # Output: 4 → [1, -1, 5, -2]
print(longest_subarray_sum_k([2, 3, 1, 2, 4, 3], 7))     # Output: 3 

