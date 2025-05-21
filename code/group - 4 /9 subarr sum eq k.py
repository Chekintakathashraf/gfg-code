"""Given an array of integers nums and an integer k, find the total number of continuous subarrays whose sum equals to k."""

def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0: 1}  # sum 0 has frequency 1
    
    for num in nums:
        curr_sum += num
        if (curr_sum - k) in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    return count

# Test cases
print(subarray_sum([1, 1, 1], 2))           # Output: 2
print(subarray_sum([1, 2, 3], 3))            # Output: 2
print(subarray_sum([1, -1, 0], 0))           # Output: 3
