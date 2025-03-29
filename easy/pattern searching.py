"""Given a text and a pattern, the task is to check if the pattern exists in the text or not.

Example 1:

Input: text = "geeksforgeeks"
       pat = "geek"
Output: 1
Explanation: "geek" exists in
"geeksforgeeks"

Example 2:

Input: text = "geeksforgeeks"
pat = "gfg"
Output: 0
Explanation: "gfg" does not exists in
"geeksforgeeks"

Your Task:  
You don't need to read input or print anything. Your task is to complete the function search() which takes the string two strings as inputs and returns 1 if the pattern is found, otherwise 0.

Expected Time Complexity: O(|text| + |pat|)
Expected Auxiliary Space: O(|text| + |pat|)"""


def search(text, pat):
    """Returns 1 if the pattern exists in the text, otherwise 0 (KMP Algorithm)."""
    n, m = len(text), len(pat)
    if m == 0:
        return 1  # An empty pattern always matches

    # Compute LPS (Longest Prefix Suffix) array
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Pattern Searching
    i = j = 0
    while i < n:
        if text[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                return 1  # Pattern found
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return 0  # Pattern not found

# Example Test Cases
print(search("geeksforgeeks", "geek"))  # Output: 1
print(search("geeksforgeeks", "gfg"))  # Output: 0
