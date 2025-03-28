"""A string s is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from s, choose the smallest element among them.

Examples:

Input: s = "29" 
Output: 30
Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 

Input: s = "15"
Output: 10
Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10."""


def round_to_nearest_ten(s):
    num = int(s)  # Convert string to integer
    remainder = num % 10

    if remainder < 5:
        return num - remainder  # Round down
    elif remainder > 5:
        return num + (10 - remainder)  # Round up
    else:
        return num - remainder  # When remainder is 5, choose the smaller multiple

# Test cases
print(round_to_nearest_ten("29"))  # Output: 30
print(round_to_nearest_ten("15"))  # Output: 10
print(round_to_nearest_ten("42"))  # Output: 40
print(round_to_nearest_ten("47"))  # Output: 50
print(round_to_nearest_ten("50"))  # Output: 50
