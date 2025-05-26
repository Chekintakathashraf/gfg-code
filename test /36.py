def max_vowels_in_substring(s, k):
    vowels = set('aeiou')
    max_vowels = 0
    current_count = 0
    max_start_index = 0    # to store start index of max vowel window

    # First window of size k
    for i in range(k):
        if s[i] in vowels:
            current_count += 1
    max_vowels = current_count


    # Slide the window
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            current_count -= 1
        if s[i] in vowels:
            current_count += 1

        if current_count > max_vowels:
            max_vowels = current_count
            max_start_index = i - k + 1  # update where the max window starts

    return max_vowels, s[max_start_index:max_start_index + k]


print(max_vowels_in_substring("abciiidef", 3))  # Output: 3 (substring = "iii")
print(max_vowels_in_substring("aeiou", 2))      # Output: 2 (any 2-letter window)
print(max_vowels_in_substring("leetcode", 3))   # Output: 2 (substring = "eet")
