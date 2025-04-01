'''Given a string S of lowercase alphabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.

Example 1:

Input:
S = machine
Output: 1
Explanation: machine is an isogram
as no letter has appeared twice. Hence
we print 1.

Example 2:

Input:
S = geeks
Output: 0
Explanation: geeks is not an isogram
as 'e' appears twice. Hence we print 0.

Your Task:
This is a function problem. You only need to complete the function isIsogram() that takes a string as a parameter and returns either true or false.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |S|'''


def isIsogram(S):
    # Create an empty set to track characters
    seen_chars = set()
    
    # Iterate through each character in the string
    for char in S:
        if char in seen_chars:
            return 0  # If the character is found in the set, it's not an isogram
        seen_chars.add(char)  # Add the character to the set
    
    return 1  # If no repeated characters are found, it's an isogram

# Example Test Cases
print(isIsogram("machine"))  # Output: 1
print(isIsogram("geeks"))    # Output: 0
print(isIsogram("acvfderty"))    # Output: 1

