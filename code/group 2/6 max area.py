def max_area(height):
    i, j = 0, len(height) - 1
    max_water = 0
    
    while i < j:
        width = j - i
        current_height = min(height[i], height[j])
        current_area = width * current_height
        max_water = max(max_water, current_area)
        
        # Move pointer of smaller height
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
            
    return max_water

print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(max_area([1,1]))                 # Output: 1
print(max_area([4,3,2,1,4]))           # Output: 16
print(max_area([1,2,1]))               # Output: 2
