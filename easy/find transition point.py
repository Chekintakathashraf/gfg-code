"""Given a sorted array, arr[] containing only 0s and 1s, find the transition point, i.e., the first index where 1 was observed, and before that, only 0 was observed.  If arr does not have any 1, return -1. If array does not have any 0, return 0.

Examples:

Input: arr[] = [0, 0, 0, 1, 1]
Output: 3
Explanation: index 3 is the transition point where 1 begins.

Input: arr[] = [0, 0, 0, 0]
Output: -1
Explanation: Since, there is no "1", the answer is -1.

Input: arr[] = [1, 1, 1]
Output: 0
Explanation: There are no 0s in the array, so the transition point is 0, indicating that the first index (which contains 1) is also the first position of the array.

Input: arr[] = [0, 1, 1]
Output: 1
Explanation: Index 1 is the transition point where 1 starts, and before it, only 0 was observed."""

def find_transition_point(arr):
    low, high = 0, len(arr) - 1

    # If first element is 1, return 0 (first occurrence of 1)
    if arr[0] == 1:
        return 0

    # If last element is 0, return -1 (no 1 found)
    if arr[-1] == 0:
        return -1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is the first occurrence of 1
        if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
            return mid

        # If mid is 0, move to right half
        elif arr[mid] == 0:
            low = mid + 1
        else:  # Move to left half
            high = mid - 1

    return -1  # If no transition point found

# Test cases
print(find_transition_point([0, 0, 0, 1, 1]))  # Output: 3
print(find_transition_point([0, 0, 0, 0]))      # Output: -1
print(find_transition_point([1, 1, 1]))         # Output: 0
print(find_transition_point([0, 1, 1]))         # Output: 1
print(find_transition_point([0, 0, 1, 1, 1]))   # Output: 2

