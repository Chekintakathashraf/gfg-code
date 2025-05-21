"""Given an integer array nums, we want to efficiently find the sum of elements between two given indices left and right (inclusive). Multiple queries like this can be asked."""

class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

# Test
nums = [1, 3, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))  # 9
print(numArray.sumRange(1, 2))  # 8
print(numArray.sumRange(0, 1))  # 4

def build_prefix(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

def sum_range(prefix, left, right):
    return prefix[right + 1] - prefix[left]

# Test
nums = [1, 3, 5]
prefix = build_prefix(nums)
print(sum_range(prefix, 0, 2))  # 9
print(sum_range(prefix, 1, 2))  # 8
print(sum_range(prefix, 0, 1))  # 4
