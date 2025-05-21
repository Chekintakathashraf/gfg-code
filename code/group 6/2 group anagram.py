"""    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.

    Two strings are anagrams if they contain the same characters in the same frequency, but possibly in different order."""
    
    

def group_anagrams(strs):
    anagram_map = {}

    for word in strs:
        key = ''.join(sorted(word))  # sorted returns a list, join it into string
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)

    return list(anagram_map.values())

# Test cases
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

