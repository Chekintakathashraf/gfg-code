"""You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element extra added in between. Return the index of the extra element.

Note: 0-based indexing is followed.

Examples

Input: a[] = [2,4,6,8,9,10,12], b[] = [2,4,6,8,10,12]
Output: 4
Explanation: In the first array, 9 is extra added and it's index is 4.

Input: a[] = [3,5,7,8,11,13], b[] = [3,5,7,11,13]
Output: 3
Explanation: In the first array, 8 is extra and it's index is 3.

Input: a[] = [3,5], b[] = [3]
Output: 1
Explanation: In the first array, 5 is extra and it's index is 1.

Constraints:
2<=arr1.size()<=105
1<=arr1[i],arr2[i]<=106 """




def find_extra_element(arr1, arr2):
    left, right = 0, len(arr2)  # Binary search range

    while left <= right:
        mid = (left + right) // 2
        if mid < len(arr2) and arr1[mid] == arr2[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Index of the extra element

# Example Test Cases
if __name__ == "__main__":
    print(find_extra_element([2,4,6,8,9,10,12], [2,4,6,8,10,12]))  # Output: 4
    print(find_extra_element([3,5,7,8,11,13], [3,5,7,11,13]))  # Output: 3
    print(find_extra_element([3,5], [3]))  # Output: 1
