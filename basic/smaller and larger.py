'''Given a sorted array arr and a value target, return an array of size 2. The first value is the number of elements less than or equal to the target, and the second value is the number of elements greater than or equal to the target.

Examples:

Input: arr[] = [1, 2, 8, 10, 11, 12, 19],  target = 0
Output: 0, 7
Explanation: There are no elements less or equal to 0 and 7 elements greater to 0.

Input: arr[] = [1, 5, 8, 12, 12, 12, 19], target = 12
Output: 6, 4
Explanation: There are 6 elements less or equal to 12 and 4 elements greater or equal to 12.

'''

import bisect

class Solution:
    def countElements(self, arr, target):
        # Find the number of elements <= target using binary search
        less_than_or_equal_count = bisect.bisect_right(arr, target)
        
        # Find the number of elements >= target using binary search
        greater_than_or_equal_count = len(arr) - bisect.bisect_left(arr, target)
        
        return less_than_or_equal_count, greater_than_or_equal_count


# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.countElements([1, 2, 8, 10, 11, 12, 19], 0))  # Output: (0, 7)
    print(solution.countElements([1, 5, 8, 12, 12, 12, 19], 12))  # Output: (6, 4)
