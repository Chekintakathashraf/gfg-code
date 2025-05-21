"""Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k."""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        seen = defaultdict(int)
        seen[0] = 1  # Handle if subarray starts from index 0

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in seen:
                count += seen[prefix_sum - k]
            seen[prefix_sum] += 1
        return count

# Test
s = Solution()
print(s.subarraySum([1, 2, 3], 3))  # Output: 2
print(s.subarraySum([1, 1, 1], 2))  # Output: 2
print(s.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4


from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    seen = defaultdict(int)
    seen[0] = 1

    for num in nums:
        prefix_sum += num
        count += seen[prefix_sum - k]
        seen[prefix_sum] += 1
    return count

# Test
print(subarray_sum([1, 2, 3], 3))  # Output: 2
print(subarray_sum([1, 1, 1], 2))  # Output: 2
print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4

#===================== without import  =================================================



def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    seen = {0: 1}  # We’ve seen 0 sum once (for subarrays that start at index 0)

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in seen:
            count += seen[prefix_sum - k]
        if prefix_sum in seen:
            seen[prefix_sum] += 1
        else:
            seen[prefix_sum] = 1
    return count

# Test cases
print(subarray_sum([1, 2, 3], 3))  # Output: 2
print(subarray_sum([1, 1, 1], 2))  # Output: 2
print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4
