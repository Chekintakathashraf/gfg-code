"""Given an array arr of positive integers. Reverse every sub-array group of size k.

Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. You shouldn't return any array, modify the given array in place.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.

Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]
Explnation: Since k is greater than array size, the entire array is reversed."""

def reverse_in_groups(arr, k):
    n = len(arr)

    for i in range(0, n, k):  # Iterate in steps of k
        left, right = i, min(i + k - 1, n - 1)  # Define the sub-array range
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]  # Swap elements
            left += 1
            right -= 1

# Test cases
arr1 = [1, 2, 3, 4, 5]
reverse_in_groups(arr1, 3)
print(arr1)  # Output: [3, 2, 1, 5, 4]

arr2 = [5, 6, 8, 9]
reverse_in_groups(arr2, 5)
print(arr2)  # Output: [9, 8, 6, 5]
