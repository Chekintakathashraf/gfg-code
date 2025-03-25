"""Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]

Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]

Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]"""


def is_subset(a, b):
    freq_a = {}  # Manual frequency dictionary
    
    # Count occurrences in a[]
    for num in a:
        if num in freq_a:
            freq_a[num] += 1
        else:
            freq_a[num] = 1

    # Check if b[] is a subset of a[]
    for num in b:
        if num in freq_a and freq_a[num] > 0:
            freq_a[num] -= 1  # Reduce count
        else:
            return False  # Element not found or exhausted in a[]

    return True

# Test Cases
print(is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))  # Output: True
print(is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))  # Output: True
print(is_subset([10, 5, 2, 23, 19], [19, 5, 3]))  # Output: False
