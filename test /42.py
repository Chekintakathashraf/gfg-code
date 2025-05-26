def find_all_subarrays(arr, target):
    prefix_map = dict({0: [-1]})
    current_sum = 0
    result = []

    for i, num in enumerate(arr):
        current_sum += num

        if (current_sum - target) in prefix_map:
            for start_idx in prefix_map[current_sum - target]:
                result.append((start_idx + 1, i))  # indices of subarray

        if current_sum not in prefix_map:
            prefix_map[current_sum] = []
        prefix_map[current_sum].append(i)

    return result



print(find_all_subarrays([1,2,3,4,6,7],10))
print(find_all_subarrays([1,2,3,6,7],15))