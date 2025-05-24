s = "this  this is only a test"

def fun(s):
    a = s.split()
    print(a)
    freeq = {}
    
    for char in a:
        freeq[char] = freeq.get(char,0) +1
    
    count = 0
    print(freeq)
    for char in freeq:
        if freeq[char] > 1:
            count = count + 1
            
    
    return count
            


print(fun(s))