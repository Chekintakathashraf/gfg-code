s = "xyzxyzz"

def fun(s):
    freeq = {}
    
    for char in s:
        freeq[char] = freeq.get(char,0) +1
    
    large = 0  
    var = None  
    for char in s:
        if freeq[char] > large:
            large = freeq[char]
            var = char
            
    return var


print(fun(s))