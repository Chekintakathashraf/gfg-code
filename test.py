s = "this is a test a is a this is only a test"



def fun(s):
    words = s.split()
    
    freeq = {}     
    print(words)       
    
    for char in words:
        freeq[char] = freeq.get(char,0) + 1
        
    sorted_freq = sorted(set(freeq.values()),reverse=True)
    
    print(sorted_freq)
    
    secondhighest = sorted_freq[0]
    
    for word in words:
        if freeq[word] == secondhighest:
            return word
    
    
print(fun(s))  
        
       