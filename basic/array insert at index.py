"""Insertion is a basic but frequently used operation. Arrays in most languages cannnot be dynamically shrinked or expanded. Here, we will work with such arrays and try to insert an element at some index.

You are given an array arr(0-based index). The size of the array is given by sizeOfArray. You need to insert an element at given index.

Example 1:

Input:
sizeOfArray = 6
arr[] = {1, 2, 3, 4, 5}
index = 5, element = 90
Output: 1 2 3 4 5 90
Explanation: 90 is inserted at index
5(0-based indexing). After inserting,
array elements are like
1, 2, 3, 4, 5, 90.

Example 2:

Input:
sizeOfArray = 6
arr[] = {1, 2, 3, 4, 5}
index = 2, element = 90
Output: 1 2 90 3 4 5
Explanation: 90 is inserted at index 
2(0-based indexing). After inserting,
array elements are like 
1, 2, 90, 3, 4, 5.

Your Task:
You don't need to read input or print anything.. The input is already taken care of by the driver code. You only need to complete the function insertAtIndex() that takes arr, sizeOfArray, index, element as input and modifies the array arr as per requirements. The printing is done by driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1)."""


class Solution:
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        # Step 1: Shift elements to the right to make space
        if index < sizeOfArray:
            arr.append(0)  # Increase array size by 1
            for i in range(sizeOfArray, index, -1):
                arr[i] = arr[i - 1]
            arr[index] = element
        else:
            # If index is equal to size, directly add the element at the end
            arr.append(element)

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    arr = [1, 2, 3, 4, 5]
    sizeOfArray = len(arr)
    index = 5
    element = 90
    solution.insertAtIndex(arr, sizeOfArray, index, element)
    print(arr)  # Output: [1, 2, 3, 4, 5, 90]
    
    # Test Case 2
    arr = [1, 2, 3, 4, 5]
    sizeOfArray = len(arr)
    index = 2
    element = 90
    solution.insertAtIndex(arr, sizeOfArray, index, element)
    print(arr)  # Output: [1, 2, 90, 3, 4, 5]
