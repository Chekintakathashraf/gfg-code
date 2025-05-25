s1 = [1,3,5,8,9]

s2 = [4,5,6,7,9,12,14]
mergedarray = []

i = 0
j = 0

while i < len(s1) and j< len(s2):
    if s1[i]< s2[j]:
        mergedarray.append(s1[i])
        i = i + 1
    else:
        mergedarray.append(s2[j])
        j = j+1
        
# Add remaining elements from s1 (if any)
while i < len(s1):
    mergedarray.append(s1[i])
    i += 1

# Add remaining elements from s2 (if any)
while j < len(s2):
    mergedarray.append(s2[j])
    j += 1

    
print(mergedarray)