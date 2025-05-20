def two_sum_sorted(nums, target):
    i, j = 0, len(nums) - 1
    
    while i < j:
        current_sum = nums[i] + nums[j]
        
        if current_sum == target:
            return [i, j]
        elif current_sum < target:
            i += 1
        else:
            j -= 1
    
    return [-1, -1]  # no pair found

print(two_sum_sorted([1, 2, 3, 4, 6], 6))    # Output: [1, 3]
print(two_sum_sorted([2, 3, 4], 6))          # Output: [0, 2]
print(two_sum_sorted([-1, 0], -1))           # Output: [0, 1]
print(two_sum_sorted([1, 2, 3], 7))          # Output: [-1, -1]

