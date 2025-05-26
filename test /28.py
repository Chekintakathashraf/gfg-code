# s = "abcabcdbb"
s = "abba"

def fun(s):
    seen_chars = set()
    start_index = 0
    max_length = 0
    max_start_index = 0  

    for end_index in range(len(s)):
        while s[end_index] in seen_chars:
            seen_chars.remove(s[start_index])
            start_index += 1

        seen_chars.add(s[end_index])
        current_window_length = end_index - start_index + 1
 
        if current_window_length > max_length:
            max_length = current_window_length
            max_start_index = start_index

    return max_length, s[max_start_index:max_start_index + max_length]


print(fun(s))