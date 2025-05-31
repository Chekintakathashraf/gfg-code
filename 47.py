def count_subarrays_with_sum_k(arr, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # sum 0 has occurred once

    for num in arr:
        prefix_sum += num

        # Check if (prefix_sum - k) was seen before
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]

        # Store/update current prefix_sum count
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

arr = [1, 0, 1, 0, 1]
k = 2
print(count_subarrays_with_sum_k(arr, k))  # Output: 4
