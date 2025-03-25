"""Given an array arr of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.

Input: arr[] = [0, 3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty.

Input: arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty."""

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Test Cases
print(find_duplicates([2, 3, 1, 2, 3]))  # Output: [2, 3]
print(find_duplicates([0, 3, 1, 2]))  # Output: []
print(find_duplicates([2]))  # Output: []



