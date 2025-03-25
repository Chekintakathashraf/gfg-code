
""" Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

"""


def second_largest(arr):
    maxim = max(arr)
    filtered_arr = [x for x in arr if x != maxim]  # Remove max elements
    return max(filtered_arr) if filtered_arr else -1  

# Test Cases
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(second_largest([10, 10, 10]))         # Output: -1
print(second_largest([5]))                  # Output: -1
print(second_largest([3, 2]))               # Output: 2

