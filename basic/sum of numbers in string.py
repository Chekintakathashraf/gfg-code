'''Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.

Examples:

Input: s = "1abc23"
Output: 24
Explanation: 1 and 23 are numbers in the string which is added to get the sum as 24.

Input: s = "geeks4geeks"
Output: 4
Explanation: 4 is the only number, so the sum is 4.'''


class Solution:
    
    # Function to calculate the sum of all numbers present in a string.
    def findSum(self, s):
        import re
        numbers = re.findall(r'\d+', s)  # Extract all numbers from the string
        return sum(map(int, numbers))  # Convert to integers and sum them

# Example usage:
sol = Solution()
print(sol.findSum("1abc23"))  # Output: 24
print(sol.findSum("geeks4geeks"))  # Output: 4
print(sol.findSum("abc"))  # Output: 0
print(sol.findSum("12xyz34"))  # Output: 46


class Solution:
    
    # Function to calculate the sum of all numbers present in a string.
    def findSum(self, s):
        total = 0
        num = 0
        
        for char in s:
            if char.isdigit():  # If the character is a digit, build the number
                num = num * 10 + int(char)
            else:
                total += num  # Add the previous number to the total
                num = 0  # Reset num for the next number
        
        total += num  # Add the last number if any
        
        return total

# Example usage:
sol = Solution()
print(sol.findSum("1abc23"))  # Output: 24
print(sol.findSum("geeks4geeks"))  # Output: 4
print(sol.findSum("abc"))  # Output: 0
print(sol.findSum("12xyz34"))  # Output: 46
