def get_subarrays_with_sum_k(arr, k):
    prefix_sum = 0
    prefix_map = {0: [-1]}  # prefix sum → list of indices
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if (prefix_sum - k) in prefix_map:
            for start_index in prefix_map[prefix_sum - k]:
                result.append(arr[start_index + 1: i + 1])  # extract subarray

        # Store current prefix sum and index
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum].append(i)
        else:
            prefix_map[prefix_sum] = [i]

    return result

arr = [1, 0, 1, 0, 1]
k = 2
subarrays = get_subarrays_with_sum_k(arr, k)
for s in subarrays:
    print(s)
