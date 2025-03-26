"""Given a string in Roman number format (s), your task is to convert it to an integer. Various symbols and their values are given below.
Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

Examples:

Input: s = "IX"
Output: 9
Explanation: IX is a Roman symbol which represents 10 – 1 = 9.

Input: s = "XL" 
Output: 40
Explanation: XL is a Roman symbol which represents 50 – 10 = 40.

Input: s = "MCMIV" 
Output: 1904
Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.

Constraints:
1<= roman number <=3999
s[i] belongs to [I, V, X, L, C, D, M]"""

def roman_to_integer(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0  # Keep track of previous value for subtraction cases

    for char in reversed(s):  # Traverse from right to left
        curr_value = roman_values[char]
        
        if curr_value < prev_value:
            total -= curr_value  # Subtract if smaller numeral precedes larger one
        else:
            total += curr_value  # Otherwise, add the value
        
        prev_value = curr_value  # Update previous value for next iteration

    return total

# 🔹 Test Cases
print(roman_to_integer("IX"))     # ✅ 9
print(roman_to_integer("XL"))     # ✅ 40
print(roman_to_integer("MCMIV"))  # ✅ 1904
print(roman_to_integer("MMXXIV")) # ✅ 2024
print(roman_to_integer("LVIII"))  # ✅ 58
