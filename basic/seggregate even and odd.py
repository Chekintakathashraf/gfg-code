'''Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Note:- You don't have to return the array, you have to modify it in-place.

Example:

Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.

Input: arr[] = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
Explanation: 0 2 4 are even and 1 3 are odd numbers.

Input: arr[] = [10, 22, 4, 6]
Output: [10, 22, 4, 6]
Explanation: Here all elements are even, so no need of segregataion'''


class Solution:
    def segregateEvenOdd(self, arr):
        # Step 1: Separate even and odd numbers
        even = [x for x in arr if x % 2 == 0]
        odd = [x for x in arr if x % 2 == 1]

        # Step 2: Sort both lists
        even.sort()
        odd.sort()

        # Step 3: Merge back to arr
        arr[:] = even + odd  # Modify array in-place

# Example usage:
arr1 = [12, 34, 45, 9, 8, 90, 3]
sol = Solution()
sol.segregateEvenOdd(arr1)
print(arr1)  # Output: [8, 12, 34, 90, 3, 9, 45]

arr2 = [0, 1, 2, 3, 4]
sol.segregateEvenOdd(arr2)
print(arr2)  # Output: [0, 2, 4, 1, 3]

arr3 = [10, 22, 4, 6]
sol.segregateEvenOdd(arr3)
print(arr3)  # Output: [10, 22, 4, 6]
