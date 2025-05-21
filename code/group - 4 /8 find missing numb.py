"""You have an array containing n distinct numbers taken from the range 0 to n. Exactly one number from this range is missing in the array. Find the missing number.
"""

def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2  # Sum from 0 to n
    return total - sum(nums)

# Test cases
print(missing_number([3, 0, 1]))       # Output: 2
print(missing_number([0, 1]))          # Output: 2
print(missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8
