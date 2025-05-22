"""Given a sorted array of integers nums and an integer target, return the index of target if it exists in nums. If the target is not present, return -1."""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Tests
print(binary_search([1, 3, 5, 7, 9], 5))  # Expected Output: 2
print(binary_search([2, 4, 6, 8, 10], 7)) # Expected Output: -1


# in for ==============================

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    max_steps = len(nums).bit_length()  # max iterations = ceil(log2(n))

    for _ in range(max_steps):
        if left > right:
            break

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
