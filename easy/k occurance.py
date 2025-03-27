"""Given an array arr and an element k. The task is to find the count of elements in the array that appear more than n/k times and n is length of arr.

Examples :

Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times.

Input: arr = [2, 3, 3, 2], k = 3
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.

Input: arr = [1, 4, 7, 7], k = 2
Output: 0
Explanation: In the given array, no element appears more than n/k times."""


def count_elements(arr, k):
    n = len(arr)
    threshold = n // k
    freq_map = {}

    # Count occurrences of each element
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Count elements that appear more than n/k times
    count = sum(1 for value in freq_map.values() if value > threshold)

    return count

# Test cases
print(count_elements([3, 1, 2, 2, 1, 2, 3, 3], 4))  # Output: 2
print(count_elements([2, 3, 3, 2], 3))             # Output: 2
print(count_elements([1, 4, 7, 7], 2))             # Output: 0
