"""Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.

Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.

Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest."""

def find_largest(arr):
    return max(arr)  # Built-in function to get the maximum element

# Test Cases
print(find_largest([1, 8, 7, 56, 90]))  # Output: 90
print(find_largest([5, 5, 5, 5]))  # Output: 5
print(find_largest([10]))  # Output: 10

def find_largest_manual(arr):
    max_element = arr[0]  # Assume first element is the largest
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Test Cases
print(find_largest_manual([1, 8, 7, 56, 90]))  # Output: 90
print(find_largest_manual([5, 5, 5, 5]))  # Output: 5
print(find_largest_manual([10]))  # Output: 10
