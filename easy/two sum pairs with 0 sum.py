"""Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].

Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].

Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n)."""


def find_unique_zero_sum_pairs(arr):
    arr.sort()  # Sort the array
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        total = arr[left] + arr[right]

        if total == 0:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1

            # Skip duplicate values to ensure unique pairs
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

    return result

# Test Cases
print(find_unique_zero_sum_pairs([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, 1]]
print(find_unique_zero_sum_pairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))  # Output: [[-6, 6], [-1, 1]]

