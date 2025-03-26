"""Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

Note: The generated output is true if you modify the given array successfully. Otherwise false.

Geeky Challenge: Solve this problem in O(n) time complexity.

Examples:

Input: arr[] = [1, 2, 3, 3, 4], a = 1, b = 2
Output: true
Explanation: One possible arrangement is: {1, 2, 3, 3, 4}. If you return a valid arrangement, output will be true.

Input: arr[] = [1, 4, 3, 6, 2, 1], a = 1, b = 3
Output: true
Explanation: One possible arrangement is: {1, 3, 2, 1, 4, 6}. If you return a valid arrangement, output will be true.

"""


def three_way_partition(arr, a, b):
    left, mid, right = 0, 0, len(arr) - 1  # Three pointers

    while mid <= right:
        if arr[mid] < a:  # Elements smaller than `a`
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] > b:  # Elements greater than `b`
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
        else:  # Elements in range [a, b]
            mid += 1
    
    return True  # The function modifies the array in-place

# 🔹 Test Cases
arr1 = [1, 2, 3, 3, 4]
print(three_way_partition(arr1, 1, 2), arr1)  # ✅ True, [1, 2, 3, 3, 4]

arr2 = [1, 4, 3, 6, 2, 1]
print(three_way_partition(arr2, 1, 3), arr2)  # ✅ True, [1, 3, 2, 1, 4, 6]
