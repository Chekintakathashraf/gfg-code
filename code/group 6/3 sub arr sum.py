"""Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals to k."""


def subarray_sum(nums, k):
    prefix_sum_count = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        diff = current_sum - k
        count += prefix_sum_count.get(diff, 0)
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count

# Test cases
print(subarray_sum([1,1,1], 2))         # Output: 2
print(subarray_sum([1,2,3], 3))         # Output: 2
print(subarray_sum([3,4,7,2,-3,1,4,2], 7))  # Output: 4
