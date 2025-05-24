s = "this is a test this is only a test"

def fun(s):
    a = s.split()
    print(a)
    freeq = {}
    for char in a:
        freeq[char] = freeq.get(char,0) +1
    
    count = 0
    word = None
    for char in a:
        if freeq[char] > count:
            count = freeq[char]
            word = char
    
    return word
            


print(fun(s))