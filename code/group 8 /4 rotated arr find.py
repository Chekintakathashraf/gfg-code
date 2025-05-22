"""Given a rotated sorted array nums (sorted in ascending order, then rotated at some pivot), find the minimum element in the array. 
What is a Rotated Sorted Array? 

Imagine you have a sorted array in ascending order: 

 

[1, 2, 3, 4, 5, 6, 7] 

 

If you "rotate" this array at some point, it means you take some elements from the front and move them to the back — or equivalently, cut the array at a pivot and swap the two parts. 

For example, if you rotate it at index 3, you take the first 3 elements [1, 2, 3] and move them after the rest: 

 

Original: [1, 2, 3, 4, 5, 6, 7] 

Rotated:  [4, 5, 6, 7, 1, 2, 3] 

 

Notice: 

    The order within the two parts remains sorted. 

    The array is not fully sorted anymore because of the rotation. 

    The smallest element is now somewhere in the middle (at index 4 here). """
    
    
    
def find_min(nums):
    left, right = 0, len(nums) - 1  # Start pointers at the ends of the array
    
    while left < right:             # Loop until left meets right
        mid = (left + right) // 2  # Find middle index
        
        # Debug print to trace values (you can remove this after understanding)
        print(f"left={left}, mid={mid}, right={right}, nums[mid]={nums[mid]}, nums[right]={nums[right]}") 
        
        if nums[mid] > nums[right]:
            # Middle element is greater than rightmost,
            # so minimum must be to the right of mid
            left = mid + 1
        else:
            # Middle element is less or equal to rightmost,
            # so minimum is at mid or to the left
            right = mid
    
    # When left == right, we've found the smallest element
    return nums[left]


print(find_min([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
print(find_min([3, 4, 5, 1, 2]))        # Output: 1
print(find_min([11, 13, 15, 17]))       # Output: 11
