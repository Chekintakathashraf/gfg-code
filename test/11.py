s = "this is a test a is a this is only a test"



def fun(s):
    words = s.split()
    
    freeq = {}     
    print(words)       
    
    for char in words:
        freeq[char] = freeq.get(char,0) + 1
    
    lists = []
    
    for word in words:
        if word not in lists:
            lists.append(word)
            
    sorted_list = sorted(lists,key=lambda x : -freeq[x])
   
    return sorted_list
   
print(fun(s))