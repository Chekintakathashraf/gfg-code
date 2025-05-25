# "reverse"

s= ['p','y','t','h','o','n']

i = 0
j = len(s)- 1

while i<j:
    s[i],s[j] = s[j],s[i]
    i=i+1
    j=j-1
    
print(s)