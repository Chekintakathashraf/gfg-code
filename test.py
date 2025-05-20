def test(s):
    freq = {}
    
    for i in s:
        freq[i] = freq.get(i,0) + 1
        
    
    top = 0
    var = ""
    
    for r,v in freq.items():
        if v > top :
            top = v
            var = r
            
    if var:
        return var[0]
            
    
print(test("success"))     
        
       