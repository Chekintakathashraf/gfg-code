# "move all zero to end"

s= [0,'p',0,'t',0,'o','n']
# s = "abcdcba"
def fun(s):
    last_zero_index = 0  # position where the next non-zero element should go

    for current in range(len(s)):
        if s[current] != 0:
            s[current], s[last_zero_index] = s[last_zero_index], s[current] 
            
            last_zero_index += 1

    return s

        
        
        
print(fun(s))