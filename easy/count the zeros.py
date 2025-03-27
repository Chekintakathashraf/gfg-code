"""Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.

Examples:

Input: arr[] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
Output: 3
Explanation: There are 3 0's in the given array.

Input: arr[] = [0, 0, 0, 0, 0]
Output: 5
Explanation: There are 5 0's in the array."""


def count_zeros(arr):
    n = len(arr)
    left, right = 0, n - 1
    first_zero_index = -1

    # Binary Search to find the first occurrence of 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            first_zero_index = mid
            right = mid - 1  # Move left to find first occurrence
        else:
            left = mid + 1  # Move right to find first 0

    # If no 0 is found, return 0
    return n - first_zero_index if first_zero_index != -1 else 0

# Test cases
print(count_zeros([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]))  # Output: 3
print(count_zeros([0, 0, 0, 0, 0]))                       # Output: 5
print(count_zeros([1, 1, 1, 1]))                          # Output: 0
