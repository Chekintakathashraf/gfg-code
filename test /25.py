s = [0,1,2,4,6,7,8]
target = 5

def fun (s,target):
    i = 0
    j = len(s) - 1

    while i<j:
        
        sumvalue = s[i]+s[j]
        
        if sumvalue == target:
            return i,j
            
        elif sumvalue > target:
            j = j-1 
            
        else:
            i = i+1


print(fun(s,target))
