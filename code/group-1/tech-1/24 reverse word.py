def reverse_words(s):
    words = s.strip().split()       # removes leading/trailing spaces + split by space
    reversed_words = words[::-1]    # reverse the list of words
    return ' '.join(reversed_words)

print(reverse_words("the sky is blue"))         # "blue is sky the"
print(reverse_words("  hello world  "))         # "world hello"
print(reverse_words("a good   example"))        # "example good a"
