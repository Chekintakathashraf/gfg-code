"""iven an array of positive integers nums and a positive integer target, find the minimal length of a contiguous subarray of which the sum is greater than or equal to target.

If there is no such subarray, return 0."""



def min_subarray_len(target, nums):
    start = 0
    total = 0
    min_len = float('inf')

    for end in range(len(nums)):
        total += nums[end]

        while total >= target:
            min_len = min(min_len, end - start + 1)
            total -= nums[start]
            start += 1

    return min_len if min_len != float('inf') else 0

# Test examples
print(min_subarray_len(7, [2,3,1,2,4,3]))    # 2
print(min_subarray_len(11, [1,1,1,1,1,1]))   # 0
print(min_subarray_len(4, [1,4,4]))          # 1

