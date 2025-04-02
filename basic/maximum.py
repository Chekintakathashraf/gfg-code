'''Given an array arr[] representing the size of candles which is reduced by 1 unit each day. The room is illuminated using all the present candles. Find the maximum number of days the room will stay illuminated (at least one candle having a size greater than 0)

Examples:

Input: arr[] = [1, 1, 2] 
Output: 2
Explanation: The candle's length is reduced by 1 in first day. So, at the end of day 1: Sizes would be [0 0 1], So, at end of second day: Sizes would be [0 0 0]. This means the room was illuminated for 2 days.

Input: arr[] = [2, 3, 4, 2, 1] 
Output: 4


'''



class Solution:
    def maxDaysIlluminated(self, arr):
        return max(arr)  # The maximum number of days the room will be illuminated

# Example usage:
sol = Solution()
print(sol.maxDaysIlluminated([1, 1, 2]))  # Output: 2
print(sol.maxDaysIlluminated([2, 3, 4, 2, 1]))  # Output: 4
print(sol.maxDaysIlluminated([5, 1, 3, 2, 4]))  # Output: 5
print(sol.maxDaysIlluminated([6, 7, 2, 5]))  # Output: 7
