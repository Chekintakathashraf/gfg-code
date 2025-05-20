def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length
        p1 = expand_around_center(i, i)
        # Even length
        p2 = expand_around_center(i, i + 1)

        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2

    return longest

print(longest_palindrome("babad"))      # "bab" or "aba"
print(longest_palindrome("cbbd"))       # "bb"
print(longest_palindrome("a"))          # "a"
print(longest_palindrome("forgeeksskeegfor"))  # "geeksskeeg"
