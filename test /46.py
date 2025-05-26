def longest_subarray_with_sum_k(arr, k):
    prefix_map = {0: -1}
    curr_sum = 0
    max_len = 0
    start_idx = -1
    end_idx = -1

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum - k in prefix_map:
            prev_index = prefix_map[curr_sum - k]
            length = i - prev_index
            if length > max_len:
                max_len = length
                start_idx = prev_index + 1
                end_idx = i

        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i

    if start_idx == -1:
        return []  # no valid subarray
    return arr[start_idx:end_idx + 1]


print(longest_subarray_with_sum_k([1, 2, 3, 1, 1, 1, 1], 5))  # Output: [3, 1, 1]
print(longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3))      # Output: 4 → [1, -1, 5, -2]
print(longest_subarray_with_sum_k([2, 3, 1, 2, 4, 3], 7))     # Output: 3 → [1, 2, 4]
