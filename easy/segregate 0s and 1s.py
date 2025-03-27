"""Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Examples :

Input: arr[] = [0, 0, 1, 1, 0]
Output: [0, 0, 0, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].

Input: arr[] = [1, 1, 1, 1]
Output: [1, 1, 1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1, 1, 1]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)"""

def segregate_zeros_and_ones(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Move left pointer if it's already 0
        while left < right and arr[left] == 0:
            left += 1
        # Move right pointer if it's already 1
        while left < right and arr[right] == 1:
            right -= 1
        # Swap if left is 1 and right is 0
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Test cases
arr1 = [0, 0, 1, 1, 0]
segregate_zeros_and_ones(arr1)
print(arr1)  # Output: [0, 0, 0, 1, 1]

arr2 = [1, 1, 1, 1]
segregate_zeros_and_ones(arr2)
print(arr2)  # Output: [1, 1, 1, 1]

arr3 = [0, 1, 0, 1, 0, 1, 0]
segregate_zeros_and_ones(arr3)
print(arr3)  # Output: [0, 0, 0, 0, 1, 1, 1]
