def move_zeros(nums):
    lastNonZeroFoundAt = 0  # pointer to place next non-zero
    
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[lastNonZeroFoundAt], nums[current] = nums[current], nums[lastNonZeroFoundAt]
            lastNonZeroFoundAt += 1

arr1 = [0, 1, 0, 3, 12]
move_zeros(arr1)
print(arr1)  # [1, 3, 12, 0, 0]

arr2 = [0, 0, 1]
move_zeros(arr2)
print(arr2)  # [1, 0, 0]

arr3 = [1, 2, 3]
move_zeros(arr3)
print(arr3)  # [1, 2, 3]
