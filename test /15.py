s1 = "abcd"
s2 = "bada"

def fun(s1,s2):
    if len(s1) != len(s2):
        return False
    
    else:
        combine = s1 + s1
        if s2 in combine:
            return True
        else :
            return False
        
print(fun(s1,s2))


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)
