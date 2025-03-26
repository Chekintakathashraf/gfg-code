"""You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.

Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original."""

def reverse_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1

# Test cases
arr1 = [1, 4, 3, 2, 6, 5]
reverse_array(arr1)
print(arr1)  # Output: [5, 6, 2, 3, 4, 1]

arr2 = [4, 5, 2]
reverse_array(arr2)
print(arr2)  # Output: [2, 5, 4]

arr3 = [1]
reverse_array(arr3)
print(arr3)  # Output: [1]
