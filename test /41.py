def find_any_subarray(arr, target):
    prefix_map = dict({0: -1})
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num
        if (current_sum - target) in prefix_map:
            start = prefix_map[current_sum - target] + 1
            end = i
            return arr[start:end+1]  # or return (start, end)
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i
    return None


print(find_any_subarray([1,2,3,4,5,6],10))
print(find_any_subarray([1,2,3,6,7],15))