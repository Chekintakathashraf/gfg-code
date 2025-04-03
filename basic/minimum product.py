'''Given an array arr of  positive integers. You need to return the minimum product of k integers of the given array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 2
Output: 2
Explanation: We will get the minimum product after multiplying 1 and 2 that is 2. So, the answer is 2.

Input: arr[] = [9, 10, 8], k = 3
Output: 720
Explanation: We have to multiply all the numbers.'''

class Solution:
    def minProduct(self, arr, k):
        # Step 1: Sort the array in ascending order
        arr.sort()
        
        # Step 2: Compute the product of the first k elements (smallest elements)
        product = 1
        for i in range(k):
            product *= arr[i]
        
        return product

# Example usage:
sol = Solution()
print(sol.minProduct([1, 2, 3, 4, 5], 2))  # Output: 2
print(sol.minProduct([9, 10, 8], 3))  # Output: 720
print(sol.minProduct([17,20, 13, 15, 12, 20, 19, 20, 13, 20, 11, 11, 16, 18, 15, 15, 12, 14], 10))  # Output: 720

