'''Given an array arr of distinct elements, the task is to return an array of all elements except the two greatest elements in sorted order.

Examples:

Input: arr[] = [2, 8, 7, 1, 5]
Output: [1, 2, 5] 
Explanation: Here we return an array contains 1 , 2, 5 and we leave two greatest elements 7 & 8. 

Input: arr[] = [7, -2, 3, 4, 9, -1]
Output: [-2, -1, 3, 4]
Explanation: Here we return an array contains -2 , -1, 3, 4 and we leave two greatest elements 7 & 9. 

Expected Time Complexity: O(nlog(n))
Expected Space Complexity: O(n)'''

class Solution:
    def removeTwoGreatest(self, arr):
        arr.sort()  # Sort the array (O(n log n))
        return arr[:-2]  # Return all elements except the last two

# Example usage:
sol = Solution()
print(sol.removeTwoGreatest([2, 8, 7, 1, 5]))  # Output: [1, 2, 5]
print(sol.removeTwoGreatest([7, -2, 3, 4, 9, -1]))  # Output: [-2, -1, 3, 4]
