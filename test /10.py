s = "this is a test a is a this is only a test"



def fun(s):
    words = s.split()
    
    freeq = {}     
    print(words)       
    
    for char in words:
        freeq[char] = freeq.get(char,0) + 1
    
    print(freeq)
    lists = []
    
    for char in words:
        if char not in lists:
            lists.append(char)
            
    print(lists)
            
    sorted_arr = sorted(lists,key=lambda x : (-freeq[x], words.index(x) ))

    return sorted_arr
print(fun(s))