"""Given an array of strings arr[]. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "".

Examples :

Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
Output: "gee"
Explanation: "gee" is the longest common prefix in all the given strings.

Input: arr[] = ["hello", "world"]
Output: ""
Explanation: There's no common prefix in the given strings."""

def longest_common_prefix(arr):
    if not arr:
        return ""

    prefix = arr[0]  # Start with the first string as the prefix

    for word in arr[1:]:  # Compare with remaining words
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = prefix[:i]  # Trim the prefix up to the matched characters
        if not prefix:  # If prefix becomes empty, no common prefix exists
            return ""

    return prefix

# Test cases
print(longest_common_prefix(["geeksforgeeks", "geeks", "geek", "geezer"]))  # Output: "gee"
print(longest_common_prefix(["hello", "world"]))  # Output: ""
print(longest_common_prefix(["apple", "ape", "april"]))  # Output: "ap"
print(longest_common_prefix(["car", "carbon", "carpenter"]))  # Output: "car"
print(longest_common_prefix([""]))  # Output: ""
print(longest_common_prefix(["same", "same", "same"]))  # Output: "same"
