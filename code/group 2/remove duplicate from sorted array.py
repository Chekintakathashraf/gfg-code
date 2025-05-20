def remove_duplicates(nums):
    if not nums:
        return 0

    write_index = 1  # start from second position

    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index

arr1 = [1, 1, 2]
length1 = remove_duplicates(arr1)
print(length1, arr1[:length1])  # Output: 2, [1, 2]

arr2 = [0,0,1,1,1,2,2,3,3,4]
length2 = remove_duplicates(arr2)
print(length2, arr2[:length2])  # Output: 5, [0,1,2,3,4]

arr3 = []
length3 = remove_duplicates(arr3)
print(length3, [])  # Output: 0, []

