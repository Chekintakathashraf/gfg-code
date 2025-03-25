"""Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

Examples:

Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and smallest positive missing number is 1.

Input: arr[] = [1, 3, 3] 
Output: [3, 2]
Explanation: Repeating number is 3 and smallest positive missing number is 2.

Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5."""


def find_missing_and_repeating(arr):
    n = len(arr)
    
    # Expected sum and sum of squares
    S_n = n * (n + 1) // 2
    S_sq_n = n * (n + 1) * (2 * n + 1) // 6
    
    # Actual sum and sum of squares
    S = sum(arr)
    S_sq = sum(x * x for x in arr)
    
    # Equations
    diff = S - S_n  # (b - a)
    sum_diff = (S_sq - S_sq_n) // diff  # (b + a)
    
    # Solve for a and b
    b = (diff + sum_diff) // 2
    a = sum_diff - b
    
    return [b, a]

# Test Cases
print(find_missing_and_repeating([2, 2]))       # Output: [2, 1]
print(find_missing_and_repeating([1, 3, 3]))    # Output: [3, 2]
print(find_missing_and_repeating([4, 3, 6, 2, 1, 1]))  # Output: [1, 5]

