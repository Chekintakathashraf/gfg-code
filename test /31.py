def longest_subarray_with_sum_at_most_k(arr, k):
    current_start = 0
    current_window_sum = 0
    max_length = 0

    for end in range(len(arr)):
        current_window_sum += arr[end]

        while current_window_sum > k:
            current_window_sum -= arr[current_start]
            current_start += 1
            
        max_length = max(max_length, end - current_start + 1)

        
    return max_length


arr = [1,2, 1, 0, 1, 1, 0]
k = 4

# arr = [2, 3, 1, 2, 4, 3]
# k = 7

# arr = [1,1,1,1]
# k = 2

print(longest_subarray_with_sum_at_most_k(arr, k))
