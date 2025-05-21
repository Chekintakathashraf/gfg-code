"""Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements between indices left and right (inclusive)."""


"""How it works:

    build_prefix prepares the prefix sum array once.

    sum_range uses the prefix array to answer queries instantly.

This approach is perfect if you don’t want to use OOP or classes."""


class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

# Test
nums = [1, 3, 5]
num_array = NumArray(nums)
print(num_array.sumRange(0, 2))  # Output: 9
print(num_array.sumRange(1, 2))  # Output: 8
print(num_array.sumRange(0, 1))  # Output: 4



def build_prefix(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

def sum_range(prefix, left, right):
    return prefix[right + 1] - prefix[left]

# Example
nums = [1, 3, 5]
prefix = build_prefix(nums)

print(sum_range(prefix, 0, 2))  # 9
print(sum_range(prefix, 1, 2))  # 8
print(sum_range(prefix, 0, 1))  # 4

