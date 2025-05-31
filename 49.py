def find_missing_number(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing_number([3, 0, 1]))       # Output: 2
print(find_missing_number([0, 1, 2, 4]))    # Output: 3
