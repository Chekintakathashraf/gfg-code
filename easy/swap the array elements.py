"""Given an array arr of positive integers. The task is to swap every ith element of the array with (i+2)th element.

Examples :

Input: arr[] = [1, 2, 3]
Output: [3, 2, 1]
Explanation: Swapping 1 and 3, makes the array [3, 2, 1]. There is only one swap possible in this array.

Input: arr[] = [1, 2, 3, 4, 5]
Output: [3, 4, 5, 2, 1]
Explanation: Swapping 1 and 3, makes the array [3, 2, 1, 4, 5]. Now, swapping 2 and 4, makes the array [3, 4, 1, 2, 5]. Again,swapping 1 and 5, makes the array [3, 4, 5, 2, 1]."""



class Solution:
    def swapEveryIthWithIPlus2(self, arr):
        n = len(arr)
        for i in range(n - 2):  # Ensure i+2 is within bounds
            arr[i], arr[i+2] = arr[i+2], arr[i]  # Swap elements
        
        return arr  # Return modified array

# Test cases
sol = Solution()
print(sol.swapEveryIthWithIPlus2([1, 2, 3]))       # Output: [3, 2, 1]
print(sol.swapEveryIthWithIPlus2([1, 2, 3, 4, 5])) # Output: [3, 4, 5, 2, 1]
