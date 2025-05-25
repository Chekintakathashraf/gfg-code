# "move all zero to end"

s= [1,2,0,'p',1,2,3,0,'t',0,'o','n']
# s = "abcdcba"
def fun(s):
    first_zero_index = 0  # position where the next non-zero element should go

    for current in range(len(s)):
        if s[current] != 0:
            s[current], s[first_zero_index] = s[first_zero_index], s[current] 
            
            first_zero_index += 1
        
  
    return s

        
        
        
print(fun(s))