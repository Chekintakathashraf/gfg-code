def min_subarray_len(target, arr):
    min_length = len(arr) + 1
    current_start = 0
    current_window_sum = 0
    min_start_index = -1  # to track where the shortest subarray starts

    for current_end in range(len(arr)):
        current_window_sum += arr[current_end]

        while current_window_sum >= target:
            if current_end - current_start + 1 < min_length:
                min_length = current_end - current_start + 1
                min_start_index = current_start

            current_window_sum -= arr[current_start]
            current_start += 1

    if min_length == len(arr) + 1:
        return 0, []  # no such subarray

    return min_length, arr[min_start_index:min_start_index + min_length]

arr = [2, 3, 1, 2, 4, 3]
target = 7

print(min_subarray_len(target, arr))
# Output: (2, [4, 3])
