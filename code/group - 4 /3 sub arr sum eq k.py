"""Given an array of integers and a target sum k, determine whether there exists a contiguous subarray (of at least size 1) whose sum is exactly equal to k"""

def has_subarray_with_sum_k(nums, k):
    prefix_sum = 0
    seen = set()
    seen.add(0)  # To handle subarray from start

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in seen:
            return True
        seen.add(prefix_sum)
    return False

# Test cases
print(has_subarray_with_sum_k([1, 2, 3], 5))     # True
print(has_subarray_with_sum_k([1, 2, 3], 7))     # False
print(has_subarray_with_sum_k([-1, -1, 3], 1))   # True


class SubarraySumChecker:
    def __init__(self, nums):
        self.nums = nums

    def has_subarray_with_sum_k(self, k):
        prefix_sum = 0
        seen = set()
        seen.add(0)

        for num in self.nums:
            prefix_sum += num
            if (prefix_sum - k) in seen:
                return True
            seen.add(prefix_sum)
        return False

# Test
checker = SubarraySumChecker([1, 2, 3])
print(checker.has_subarray_with_sum_k(5))  # True
