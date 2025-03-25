"""Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].

Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6]. 

Input: arr = [1, 2, 3]
Output: true
Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right."""

def find_peak_element(arr):
    n = len(arr)
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
            return mid  # Found a peak
        
        # If the right neighbor is greater, move right
        if mid < n - 1 and arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # This should never happen since a peak is guaranteed

# Test Function
def validate_peak(arr, index):
    if index == -1 or index >= len(arr):
        return False
    if index > 0 and arr[index] <= arr[index - 1]:
        return False
    if index < len(arr) - 1 and arr[index] <= arr[index + 1]:
        return False
    return True  # Valid peak

# Test Cases
arr1 = [1, 2, 4, 5, 7, 8, 3]
arr2 = [10, 20, 15, 2, 23, 90, 80]
arr3 = [1, 2, 3]

# Run Tests
index1 = find_peak_element(arr1)
index2 = find_peak_element(arr2)
index3 = find_peak_element(arr3)

print(validate_peak(arr1, index1))  # Output: True
print(validate_peak(arr2, index2))  # Output: True
print(validate_peak(arr3, index3))  # Output: True
