"""Given a rotated sorted array nums and a target value, find the index of target in nums.
If the target is not present, return -1."""


def search_in_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Test cases
print(search_in_rotated([4,5,6,7,0,1,2], 0))  # Output: 4
print(search_in_rotated([4,5,6,7,0,1,2], 3))  # Output: -1
print(search_in_rotated([1], 0))              # Output: -1
