"""Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.

Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3."""

def count_occurrences(arr, target):
    def binary_search(find_first):
        low, high, result = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid  # Store the position
                if find_first:
                    high = mid - 1  # Move left to find first occurrence
                else:
                    low = mid + 1   # Move right to find last occurrence
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    first = binary_search(True)
    if first == -1:  # Target not found
        return 0
    last = binary_search(False)
    return last - first + 1

# Test cases
print(count_occurrences([1, 1, 2, 2, 2, 2, 3], 2))  # Output: 4
print(count_occurrences([1, 1, 2, 2, 2, 2, 3], 4))  # Output: 0
print(count_occurrences([8, 9, 10, 12, 12, 12], 12)) # Output: 3
