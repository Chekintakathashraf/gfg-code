'''Given an array arr of integers. First sort the array then find whether three numbers are such that the sum of two elements equals the third element.

Example:

Input: arr[] = [1, 2, 3, 4, 5]
Output: true
Explanation: The pair (1, 2) sums to 3.

Input: arr[] = [3, 4, 5]
Output: false
Explanation: No triplets satisfy the condition.'''


class Solution:
    def checkTripletSum(self, arr):
        arr.sort()  # First, sort the array (O(n log n))
        n = len(arr)
        
        # Iterate from the last element (which should be the largest in sorted array)
        for i in range(n - 1, 1, -1):  # Start from the last index
            target = arr[i]  # The number to check if it can be formed by two others
            left, right = 0, i - 1  # Two pointers

            while left < right:
                sum_lr = arr[left] + arr[right]
                if sum_lr == target:
                    return True  # Found a valid triplet
                elif sum_lr < target:
                    left += 1  # Move left pointer to increase sum
                else:
                    right -= 1  # Move right pointer to decrease sum

        return False  # No valid triplet found

# Example usage:
sol = Solution()
print(sol.checkTripletSum([1, 2, 3, 4, 5]))  # Output: True (1 + 2 = 3)
print(sol.checkTripletSum([3, 4, 5]))  # Output: False
print(sol.checkTripletSum([10, 20, 30, 50, 80]))  # Output: True (30 + 50 = 80)
print(sol.checkTripletSum([5, 10, 15, 25]))  # Output: False
