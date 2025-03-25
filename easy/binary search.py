"""Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

Note: If multiple occurrences are there, please return the smallest index.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: 3
Explanation: 4 appears at index 3.

Input: arr[] = [11, 22, 33, 44, 55], k = 445
Output: -1
Explanation: 445 is not present.

Input: arr[] = [1, 1, 1, 1, 2], k = 1
Output: 0
Explanation: 1 appears at index 0.

Note: Try to solve this problem in constant space i.e O(1)"""


def find_first_occurrence(arr, k):
    low, high = 0, len(arr) - 1
    first_index = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            first_index = mid  # Update first occurrence
            high = mid - 1  # Search in the left half
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    
    return first_index

# Test Cases
print(find_first_occurrence([1, 2, 3, 4, 5], 4))  # Output: 3
print(find_first_occurrence([11, 22, 33, 44, 55], 445))  # Output: -1
print(find_first_occurrence([1, 1, 1, 1, 2], 1))  # Output: 0
