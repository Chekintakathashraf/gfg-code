def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for ch1, ch2 in zip(s, t):
        if ch1 in map_s_t and map_s_t[ch1] != ch2:
            return False
        if ch2 in map_t_s and map_t_s[ch2] != ch1:
            return False

        map_s_t[ch1] = ch2
        map_t_s[ch2] = ch1

    return True

print(is_isomorphic("egg", "add"))     # True
print(is_isomorphic("foo", "bar"))     # False
print(is_isomorphic("paper", "title")) # True
print(is_isomorphic("ab", "aa"))       # False

