s = "programming"

def fun(s):
    freeq = {}
    
    for char in s:
        freeq[char] = freeq.get(char,0) +1
    
    a = []
    for char in s:
        if freeq[char] > 1 and  char not in a:
            a.append(char)
    
    return a


print(fun(s))