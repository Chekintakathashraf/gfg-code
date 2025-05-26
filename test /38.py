def fun(arr, k):
    max_sum = current_window_sum = sum(arr[:k])  # initial window sum (first k elements)
    max_start_index = 0                           # store where the max sum window starts

    for end_index in range(k, len(arr)):
        # Move the window by 1: add next, remove previous start
        current_window_sum = current_window_sum + arr[end_index] - arr[end_index - k]
        
        if current_window_sum > max_sum:
            max_sum = current_window_sum
            max_start_index = end_index - k + 1  # update where the max window starts

    return max_sum, arr[max_start_index:max_start_index + k]  # return both sum and subarray


arr = [2,1,5,1,3,2]
k = 3

print(fun(arr, k)) 