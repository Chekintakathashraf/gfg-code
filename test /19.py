s="hello"

def fun(s):
    
    vowels = []
    consonants = []
    
    for char in s:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels.append(char)
            else:
                consonants.append(char)
                
    return vowels,consonants

print(fun(s))