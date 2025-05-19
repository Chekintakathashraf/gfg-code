def first_unique_char(s: str) -> int:
    for i in s:
        count = 0
        for n in s :
            if i == n:
                count = count +1
                
        if count == 1:
            return s.index(i)
    else:
        return -1
        
s =  "leetcode"
s = "loveleetcode"
s = "aabb"
print(first_unique_char(s))
      
def first_unique_char(s: str) -> int:
    freq = {}

    # First pass: Count each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Second pass: Find the first character with count 1
    for index in range(len(s)):
        if freq[s[index]] == 1:
            return index

    return -1

from collections import Counter

def first_unique_char(s: str) -> int:
    freq = Counter(s)  # Count frequency of each character
    for idx, char in enumerate(s):
        if freq[char] == 1:
            return idx
    return -1

         
        
