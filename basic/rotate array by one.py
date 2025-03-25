"""Given an array arr, rotate the array by one position in clockwise direction.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
Explanation: After rotating clock-wise 3 comes in first position.

"""

def rotate_by_one(arr):
    if not arr or len(arr) == 1:
        return  # No need to rotate an empty or single-element array

    last_element = arr[-1]  # Store the last element
    for i in range(len(arr) - 1, 0, -1):  # Shift elements to the right
        arr[i] = arr[i - 1]
    arr[0] = last_element  # Place the last element at the first position

# Test cases
arr1 = [1, 2, 3, 4, 5]
rotate_by_one(arr1)
print(arr1)  # Output: [5, 1, 2, 3, 4]

arr2 = [9, 8, 7, 6, 4, 2, 1, 3]
rotate_by_one(arr2)
print(arr2)  # Output: [3, 9, 8, 7, 6, 4, 2, 1]
