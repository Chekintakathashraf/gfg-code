"""Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

Examples:

Input: arr[] = [111, 222, 333, 444, 555]
Output: true
Explanation:
arr[0] = 111, which is a palindrome number.
arr[1] = 222, which is a palindrome number.
arr[2] = 333, which is a palindrome number.
arr[3] = 444, which is a palindrome number.
arr[4] = 555, which is a palindrome number.
As all numbers are palindrome so This will return true.

Input: arr[] = [121, 131, 20]
Output: false
Explanation: 20 is not a palindrome hence the output is false.

Expected Time Complexity: O(nlogn)
Expected Space Complexity: O(1)"""


class Solution:
    def isPalindrome(self, num):
        return str(num) == str(num)[::-1]

    def allPalindromes(self, arr):
        return all(self.isPalindrome(num) for num in arr)

# Example usage
sol = Solution()

arr1 = [111, 222, 333, 444, 555]
print(sol.allPalindromes(arr1))  # Output: True

arr2 = [121, 131, 20]
print(sol.allPalindromes(arr2))  # Output: False
