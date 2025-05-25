s = "this is a test a is a this is only a test"

def fun(s):
    a = s.split()
    print(a)
    freeq = {}
    for char in a:
        freeq[char] = freeq.get(char,0) +1
    
    newfreeq = {}
    for u,v in freeq.items():
        if v in newfreeq:
            newfreeq[v] = newfreeq[v].append(u)
        else:
            newfreeq[v] = [u]
    
    return newfreeq
            


print(fun(s))