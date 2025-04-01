"""Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the exceptional number.

Example 1:

Input:
N = 7
Arr[] = {1, 2, 3, 2, 3, 1, 3}
Output: 3
Explaination: 3 occurs three times.


Example 2:

Input:
N = 7
Arr[] = {5, 7, 2, 7, 5, 2, 5}
Output: 5
Explaination: 5 occurs three times.


Your Task:
You don't need to read input or print anything. Your task is to complete the function getOddOccurrence() which takes arr[] and n as input parameters and returns the exceptional number.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)"""


class Solution:
    def getOddOccurrence(self, arr, n):
        result = 0
        for num in arr:
            result ^= num  # XOR all numbers
        return result  # The remaining number is the answer

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    arr = [1, 2, 3, 2, 3, 1, 3]
    n = len(arr)
    print(solution.getOddOccurrence(arr, n))  # Output: 3

    # Test Case 2
    arr = [5, 7, 2, 7, 5, 2, 5]
    n = len(arr)
    print(solution.getOddOccurrence(arr, n))  # Output: 5
