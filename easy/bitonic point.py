"""Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].

Input: arr[] = [10, 20, 30, 40, 50]
Output: 50
Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.

Input: arr[] = [120, 100, 80, 20, 0]
Output: 120
Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0]."""

def find_bitonic_point(arr):
    n = len(arr)
    if n == 1:
        return arr[0]  # Single element is the max

    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if mid is the bitonic point
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]

        # If the mid element is in the increasing part, move right
        elif mid < n - 1 and arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Should never reach here

# Test cases
print(find_bitonic_point([1, 2, 4, 5, 7, 8, 3]))  # Output: 8
print(find_bitonic_point([10, 20, 30, 40, 50]))   # Output: 50
print(find_bitonic_point([120, 100, 80, 20, 0]))  # Output: 120
print(find_bitonic_point([3, 5, 7, 9, 6, 4, 2]))  # Output: 9
print(find_bitonic_point([1, 3, 5, 7, 9]))        # Output: 9 (Strictly increasing case)
