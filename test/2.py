s = "abcde"

def fun(s):
    a = set()
    
    for char in s:
        if char in a:
            return char
        a.add(char)
        
    else:
        return "None"
    
print(fun(s))