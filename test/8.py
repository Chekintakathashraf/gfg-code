s = "this is a test a is a this is only a test"

def fun(s):
    a = s.split()
    print(a)
    freeq = {}
    for char in a:
        freeq[char] = freeq.get(char,0) +1
    
    newfreeq = []
    
    for char in a:
        if freeq[char] == 1 and char not in newfreeq:
            newfreeq.append(char)
    
    return newfreeq
            


print(fun(s))