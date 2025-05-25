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
            
    sortedList = sorted(lists,key=lambda x : (len(x),-freeq[x],words.index(x)))
    
    return sortedList

s = "dog cat mouse cat dog dog"
s = "apple banana apple orange banana apple"
print(fun(s))