"""You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.

Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.

Input: s = "a"
Output: true
Explanation: A single-character string is always a palindrome.

Input: s = "acbca"
Output: true
Explanation: "acbca" reads the same forwards and backwards, so it is a palindrome."""



def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Test cases
print(is_palindrome("abba"))  # Output: True
print(is_palindrome("abc"))   # Output: False
print(is_palindrome("a"))     # Output: True
print(is_palindrome("acbca")) # Output: True
