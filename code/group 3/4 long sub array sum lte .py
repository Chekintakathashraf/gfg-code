"""You want to find the longest stretch of numbers (subarray) where the total sum is at most k.

You’ll use a sliding window to expand the window as long as the sum is within k, and shrink it from the left when it goes over."""



def longest_subarray_sum_leq_k(arr, k):
    start = 0
    current_sum = 0
    max_len = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > k:
            current_sum -= arr[start]
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len

# Test examples
print(longest_subarray_sum_leq_k([1, 2, 1, 0, 1, 1, 0], 4))   # 6
print(longest_subarray_sum_leq_k([2, 3, 1, 2, 4, 3], 7))     # 4
print(longest_subarray_sum_leq_k([1, 1, 1, 1], 2))           # 2
