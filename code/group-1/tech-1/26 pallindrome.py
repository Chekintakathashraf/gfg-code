# Code (Basic Case-Sensitive):

def is_palindrome(s):
    return s == s[::-1]

#Code (Ignore case and spaces):

def is_palindrome_cleaned(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("madam"))                   # True
print(is_palindrome("hello"))                   # False
print(is_palindrome_cleaned("A man a plan a canal Panama"))  # True
print(is_palindrome_cleaned("No lemon, no melon"))           # True


