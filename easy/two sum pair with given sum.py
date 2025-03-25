"""Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct indices such that the sum of there elements is equals to target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.

Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.

Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[]."""


def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True  # Found a pair
        seen.add(num)
    return False  # No pair found

# Test cases
print(has_pair_with_sum([1, 4, 45, 6, 10, 8], 16))  # Output: True
print(has_pair_with_sum([1, 2, 4, 3, 6], 11))       # Output: False
print(has_pair_with_sum([11], 11))                  # Output: False
