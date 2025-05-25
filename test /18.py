
s = "programming"

def fun(s):
    
    string = ""
    
    for char in s:
        if char not in string:
            string = string+char
            
    return string
    

def fun(s):
    
    lists = []
    
    for char in s:
        if char not in lists:
            lists.append(char)
            
    return "".join(lists)              
            
print(fun(s))