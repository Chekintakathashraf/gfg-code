s = "this is a test a is a this is only a test"

def fun(s):
    a = s.split()
    print(a)
    freeq = {}
    
    for char in a:
        freeq[char] = freeq.get(char,0) +1
    print(freeq) 
    sorted_value = sorted(set(freeq.values()),reverse=True)
    
    if len(sorted_value) < 2:
        return None
    
    secondhighestvalue = sorted_value[1]
   
    for char in a:
        if freeq[char] == secondhighestvalue :
            return char
    
   
            


print(fun(s))