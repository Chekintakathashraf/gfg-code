def count_subarrays(arr, target):
    prefix_map = {0: 1}  # frequency of prefix sums
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num
        if (current_sum - target) in prefix_map:
            count += prefix_map[current_sum - target]
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count


print(count_subarrays([1,2,3,4,6,7],10))
print(count_subarrays([1,2,3,6,7],15))