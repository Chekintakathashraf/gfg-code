"""Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array.

Examples :

Input: arr = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return 1 after modifying the array, the driver code will print the modified array elements.

Input: arr = [1, 2, 4]
Output: [1, 2, 4]
Explation:  As the array does not contain any duplicates so you should return 3."""

def remove_duplicates(arr):
    if not arr:
        return 0  # If array is empty, return size 0
    
    unique_index = 0  # Pointer for placing unique elements

    for i in range(1, len(arr)):  # Traverse the array from index 1
        if arr[i] != arr[unique_index]:  # If new distinct element found
            unique_index += 1
            arr[unique_index] = arr[i]  # Move the unique element forward

    return unique_index + 1  # The size of the modified array (1-based index)

# Test cases
arr1 = [2, 2, 2, 2, 2]
size1 = remove_duplicates(arr1)
print(arr1[:size1])  # Output: [2]

arr2 = [1, 2, 4]
size2 = remove_duplicates(arr2)
print(arr2[:size2])  # Output: [1, 2, 4]

arr3 = [1, 1, 2, 2, 3, 3, 4, 5, 5]
size3 = remove_duplicates(arr3)
print(arr3[:size3])  # Output: [1, 2, 3, 4, 5]
