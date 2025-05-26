def exists_subarray(arr, target):
    prefix_map = set([0])
    current_sum = 0

    for num in arr:
        current_sum += num
        if (current_sum - target) in prefix_map:
            return True
        prefix_map.add(current_sum)

    return False

print(exists_subarray([1,2,3,4,5,6],10))
print(exists_subarray([1,2,3,6,7],15))


