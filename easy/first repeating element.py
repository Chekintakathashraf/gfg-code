"""Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

Note:- The position you return should be according to 1-based indexing. 

Examples:

Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
Output: 2
Explanation: 5 appears twice and its first appearance is at index 2 which is less than 3 whose first the occurring index is 3.

Input: arr[] = [1, 2, 3, 4]
Output: -1
Explanation: All elements appear only once so answer is -1"""

def first_repeating_element(arr):
    index_map = {}  # Dictionary to store first occurrence index
    min_index = float('inf')  # Store minimum index of repeating element

    for i, num in enumerate(arr):
        if num in index_map:
            min_index = min(min_index, index_map[num])  # Update minimum index
        else:
            index_map[num] = i + 1  # Store first occurrence (1-based index)

    return min_index if min_index != float('inf') else -1

# Test cases
print(first_repeating_element([1, 5, 3, 4, 3, 5, 6]))  # Output: 2
print(first_repeating_element([1, 2, 3, 4]))           # Output: -1
print(first_repeating_element([7, 1, 2, 1, 7, 3, 4]))  # Output: 2

