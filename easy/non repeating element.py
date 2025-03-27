"""Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

Note: The array consists of only positive and negative integers and not zero.

Examples:

Input: arr[] = [-1, 2, -1, 3, 2]
Output: 3
Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3. 

Input: arr[] = [1, 1, 1]
Output: 0
Explanation: There is not present any non-repeating element so answer should be 0.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n)."""


def first_non_repeating(arr):
    count_map = {}

    # Count occurrences of each element
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1

    # Find the first non-repeating element
    for num in arr:
        if count_map[num] == 1:
            return num

    return 0  # No non-repeating element found

# Test cases
print(first_non_repeating([-1, 2, -1, 3, 2]))  # Output: 3
print(first_non_repeating([1, 1, 1]))          # Output: 0
print(first_non_repeating([4, 5, 6, 7, 8, 5, 6]))  # Output: 4
print(first_non_repeating([10, -2, 10, -2, 3]))  # Output: 3
