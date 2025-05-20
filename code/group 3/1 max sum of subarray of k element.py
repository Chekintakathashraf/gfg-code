"""Given an array of integers arr and a number k, find the maximum sum of any contiguous subarray of size k.

A subarray means a continuous sequence of elements inside the array."""

def max_sum_subarray_k(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]  # Add right element

        # When window size reaches k, slide it
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update max sum
            window_sum -= arr[start]            # Remove left element
            start += 1                         # Slide window right

    return max_sum

# Test examples
print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))    # 9
print(max_sum_subarray_k([1, 9, -1, -2, 7, 3], 4))  # 13

