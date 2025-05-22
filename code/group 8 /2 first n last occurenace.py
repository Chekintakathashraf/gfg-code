"""

Given a sorted array nums and a target value, find the first and last positions (indices) of the target in nums.
If the target is not present, return [-1, -1]."""

def find_first(nums, target):
    left, right = 0, len(nums) - 1
    first = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            first = mid
            right = mid - 1  # continue searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return first

def find_last(nums, target):
    left, right = 0, len(nums) - 1
    last = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            last = mid
            left = mid + 1  # continue searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return last

def search_range(nums, target):
    return [find_first(nums, target), find_last(nums, target)]

# Test cases
print(search_range([2, 4, 4, 4, 6, 8], 4))  # Output: [1, 3]
print(search_range([1, 3, 5, 7], 2))        # Output: [-1, -1]
