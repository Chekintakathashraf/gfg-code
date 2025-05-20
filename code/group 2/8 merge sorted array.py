def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append leftover elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

print(merge_sorted_arrays([1,3,5], [2,4,6]))      # Output: [1,2,3,4,5,6]
print(merge_sorted_arrays([0,2,4], [1,3,5,7]))    # Output: [0,1,2,3,4,5,7]
print(merge_sorted_arrays([], [1,2,3]))           # Output: [1,2,3]
print(merge_sorted_arrays([1,2,3], []))           # Output: [1,2,3]

