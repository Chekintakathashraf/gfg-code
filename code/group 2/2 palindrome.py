def is_palindrome(s):
    i = 0
    j = len(s) - 1
    
    while i < j:
        if s[i] != s[j]:
            return False  # Not palindrome if mismatch
        i += 1
        j -= 1
    return True


print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("a"))        # True
print(is_palindrome(""))         # True
