"""Given a sorted array nums and a target value, return the index where the target should be inserted in order to maintain the sorted order.
If the target is already in the array, return its index."""


def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # target not found, left is insert position
    return left

# Test cases
print(search_insert([1, 3, 5, 6], 5))  # Output: 2
print(search_insert([1, 3, 5, 6], 2))  # Output: 1
print(search_insert([1, 3, 5, 6], 7))  # Output: 4

