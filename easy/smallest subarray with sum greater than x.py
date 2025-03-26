"""Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

Examples:

Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: Minimum length subarray is [4, 45, 6]

Input: x = 100, arr[] = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray exist"""


def smallest_subarray_with_sum(x, arr):
    n = len(arr)
    min_length = float("inf")
    start, end, curr_sum = 0, 0, 0

    while end < n:
        # Expand the window by adding arr[end]
        curr_sum += arr[end]
        end += 1

        # Shrink window while sum is greater than x
        while curr_sum > x:
            min_length = min(min_length, end - start)  # Update min length
            curr_sum -= arr[start]  # Remove arr[start] from sum
            start += 1

    return min_length if min_length != float("inf") else 0

# Test cases
print(smallest_subarray_with_sum(51, [1, 4, 45, 6, 0, 19]))  # Output: 3
print(smallest_subarray_with_sum(100, [1, 10, 5, 2, 7]))     # Output: 0
print(smallest_subarray_with_sum(9, [1, 2, 3, 4, 5]))        # Output: 2 (4+5)
