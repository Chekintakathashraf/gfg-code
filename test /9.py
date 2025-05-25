s = "this is a test a is a this is only a test"

   

def fun(s):
    words = s.split()
    
    freeq = {}    
    
    for char in words:
        freeq[char] = freeq.get(char,0) + 1
    
    # freeq_list = sorted(set(freeq.values()),key=lambda x : -x)
    freeq_list = sorted(set(freeq.values()), reverse=True)
    

    if len(freeq_list) < 2:
        return None
    
    second_freeq = freeq_list[1]
    
    for i in words:
        if freeq[i] == second_freeq:
            return i
    
   


print(fun(s))