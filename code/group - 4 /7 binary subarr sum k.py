"""Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum equal to goal."""


# with import
from collections import defaultdict

def numSubarraysWithSum(nums, goal):
    count = defaultdict(int)
    count[0] = 1
    current_sum = 0
    result = 0

    for num in nums:
        current_sum += num
        result += count[current_sum - goal]
        count[current_sum] += 1
    
    return result

# Test Cases
print(numSubarraysWithSum([1,0,1,0,1], 2))  # Output: 4
print(numSubarraysWithSum([0,0,0,0,0], 0))  # Output: 15


#wo

def numSubarraysWithSum(nums, goal):
    count = {0: 1}
    current_sum = 0
    result = 0

    for num in nums:
        current_sum += num
        if current_sum - goal in count:
            result += count[current_sum - goal]
        if current_sum in count:
            count[current_sum] += 1
        else:
            count[current_sum] = 1
    
    return result

print(numSubarraysWithSum([1,0,1,0,1], 2))  # Output: 4
print(numSubarraysWithSum([0,0,0,0,0], 0))  # Output: 15