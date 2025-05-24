
s = "leetcode"

def fun(s):
    freeq = {}
    
    for char in s:
        freeq[char] = freeq.get(char,0) + 1
    
    for i,char in enumerate(s):
        if freeq[char] == 1:
            return i
       
            
            
print(fun(s))