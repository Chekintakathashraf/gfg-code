"""You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s."""

def move_zeros_to_end(arr):
    n = len(arr)
    left = 0  # Pointer for the position to place non-zero elements

    # Move non-zero elements forward
    for right in range(n):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]  # Swap
            left += 1  # Move left pointer forward

# Test cases
arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
move_zeros_to_end(arr1)
print(arr1)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

arr2 = [10, 20, 30]
move_zeros_to_end(arr2)
print(arr2)  # Output: [10, 20, 30]

arr3 = [0, 0]
move_zeros_to_end(arr3)
print(arr3)  # Output: [0, 0]
