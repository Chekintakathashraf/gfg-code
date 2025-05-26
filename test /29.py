

def min_subarray_len(target, arr):
  
    min_length = len(arr) + 1
    current_start = 0
    current_window_sum = 0

    for current_end in range(len(arr)):
        current_window_sum += arr[current_end]

        while current_window_sum >= target:
            # directly update min_length using min()
            min_length = min(min_length, current_end - current_start + 1)
            current_window_sum -= arr[current_start]
            current_start += 1

    return min_length if min_length != len(arr) + 1 else 0

arr = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(target, arr))  # Output: 2

