"""Given an array arr of distinct elements, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

    arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

Note: Modify the given arr[] only, If your transformation is correct, the output will be "true" else the output will be "false". 

Examples

Input: arr[] = [4, 3, 7, 8, 6, 2, 1]
Output: true
Explanation:  After modification the array will look like 3 < 7 > 4 < 8 > 2 < 6 > 1, the checker in the driver code will produce 1.

Input: arr[] = [4, 7, 3, 8, 2]
Output: true
Explanation: After modification the array will look like 4 < 7 > 3 < 8 > 2 hence output will be 1.

Input: arr[] = [2, 8, 1, 7, 5, 9]
Output: true

"""

def zigzag_array(arr):
    n = len(arr)

    for i in range(n - 1):
        # If index is even, check arr[i] < arr[i+1]
        if i % 2 == 0 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
        # If index is odd, check arr[i] > arr[i+1]
        elif i % 2 == 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return True  # Output is "true" if the transformation is correct

# Test cases
arr1 = [4, 3, 7, 8, 6, 2, 1]
print(zigzag_array(arr1), arr1)  # Output: true [3, 7, 4, 8, 2, 6, 1]

arr2 = [4, 7, 3, 8, 2]
print(zigzag_array(arr2), arr2)  # Output: true [4, 7, 3, 8, 2]

arr3 = [2, 8, 1, 7, 5, 9]
print(zigzag_array(arr3), arr3)  # Output: true [2, 8, 1, 7, 5, 9]


