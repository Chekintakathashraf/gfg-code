"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum."""

def max_subarray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        # Extend current subarray or start new at num
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(max_subarray([1]))  # Output: 1
print(max_subarray([-1, -2, -3]))  # Output: -1
