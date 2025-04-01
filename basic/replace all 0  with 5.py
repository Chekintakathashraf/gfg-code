"""You are given an integer n. You need to convert all zeroes of n to 5.

Examples:

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.

Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121."""


class Solution:
    def convertFive(self, n: int) -> int:
        # Convert integer to string, replace '0' with '5', and convert back to integer
        return int(str(n).replace('0', '5'))

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n = 1004
    print(solution.convertFive(n))  # Output: 1554
    
    # Test Case 2
    n = 121
    print(solution.convertFive(n))  # Output: 121
    
    # Test Case 3
    n = 0
    print(solution.convertFive(n))  # Output: 5
    
    # Test Case 4
    n = 5050
    print(solution.convertFive(n))  # Output: 5555



