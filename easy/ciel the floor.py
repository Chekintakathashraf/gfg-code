"""Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

    Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
    Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.

Examples:

Input: x = 7 , arr[] = [5, 6, 8, 9, 6, 5, 5, 6]
Output: 6, 8
Explanation: Floor of 7 is 6 and ceil of 7 is 8.

Input: x = 10 , arr[] = [5, 6, 8, 8, 6, 5, 5, 6]
Output: 8, -1
Explanation: Floor of 10 is 8 but ceil of 10 is not possible.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)"""

def find_floor_ceil(arr, x):
    floor, ceil = -1, -1  # Default values
    
    for num in arr:
        if num <= x and (floor == -1 or num > floor):
            floor = num
        if num >= x and (ceil == -1 or num < ceil):
            ceil = num
    
    return [floor, ceil]

# 🔹 Test Cases
print(find_floor_ceil([5, 6, 8, 9, 6, 5, 5, 6], 7))   # ✅ Output: [6, 8]
print(find_floor_ceil([5, 6, 8, 8, 6, 5, 5, 6], 10))  # ✅ Output: [8, -1]
print(find_floor_ceil([3, 10, 20, 30], 15))           # ✅ Output: [10, 20]
print(find_floor_ceil([2, 4, 6, 8], 1))               # ✅ Output: [-1, 2]
