"""Given a string s without spaces, the task is to remove all duplicate characters from it, keeping only the first occurrence.

Note: The original order of characters must be kept the same. 

Examples :

Input: s = "zvvo"
Output: "zvo"
Explanation: Only keep the first occurrence

Input: s = "gfg"
Output: "gf"
Explanation: Only keep the first occurrence"""


def remove_duplicates(s):
    seen = set()  # To track seen characters
    result = []   # To store unique characters in order

    for char in s:
        if char not in seen:
            seen.add(char)  # Mark character as seen
            result.append(char)  # Add to result
    
    return "".join(result)  # Convert list to string

# Test cases
print(remove_duplicates("zvvo"))  # Output: "zvo"
print(remove_duplicates("gfg"))   # Output: "gf"
print(remove_duplicates("abcabc")) # Output: "abc"

