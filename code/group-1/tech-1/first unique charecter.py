""" 
first charecter - frequency ==1 - 
"""


def find_first_char(s):
    
    freq = {}
    
    for i in s:
        freq[i] = freq.get(i,0) + 1
        
    
    for i in s:
        if freq[i] == 1:
           return i
       
    return "None"

s = "swiss"

# s = "aabbcc"

print(find_first_char(s))