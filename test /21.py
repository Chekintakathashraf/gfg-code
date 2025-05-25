# "pallindrom"

# s= ['p','y','t','h','o','n']
s = "abcdcba"
def fun(s):
    i = 0
    j = len(s)- 1

    while i<j:
        if s[i] != s[j]:
            return False
        else:
            i = i+1
            j = j-1
    return True
print(fun(s))