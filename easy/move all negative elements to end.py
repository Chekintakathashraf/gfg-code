"""Given an unsorted array arr[ ] having both negative and positive integers. The task is to place all negative elements at the end of the array without changing the order of positive elements and negative elements.

Note: Don't return any array, just in-place on the array.

Examples:

Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
Output : [1, 3, 2, 11, 6, -1, -7, -5]
Explanation: By doing operations we separated the integers without changing the order.

Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
Output : [7, 9, 10, 11, -5, -3, -4, -1]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)"""

def move_negatives_to_end(arr):
    n = len(arr)
    pos = []  # Store positive numbers
    neg = []  # Store negative numbers

    # Step 1: Separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    # Step 2: Merge both lists back into the original array
    arr[:len(pos)] = pos
    arr[len(pos):] = neg

# Test cases
arr1 = [1, -1, 3, 2, -7, -5, 11, 6]
move_negatives_to_end(arr1)
print(arr1)  # Output: [1, 3, 2, 11, 6, -1, -7, -5]

arr2 = [-5, 7, -3, -4, 9, 10, -1, 11]
move_negatives_to_end(arr2)
print(arr2)  # Output: [7, 9, 10, 11, -5, -3, -4, -1]
