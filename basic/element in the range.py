'''Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range (inclusive).

Note: If the array contains all elements in the given range return true otherwise return false.

Examples :

Input: n = 7, A = 2, B = 5, arr[] =  {1, 4, 5, 2, 7, 8, 3}
Output: True
Explanation: It has all elements between range 2-5 i.e 2,3,4,5.

Input: n = 7, A = 2, B = 6, arr[] = {1, 4, 5, 2, 7, 8, 3}
Output: False
Explanation: The array does not contain 6 hence it do not contains all elements in the range 2-6, the output is No.


Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function check_elements() that takes array arr, integer N, integer A, and integer B  as parameters and returns the boolean True if array elements contain all elements in the given range else boolean False.

 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


'''

def check_elements(arr, n, A, B):
    # Create a set from the array for fast lookup
    arr_set = set(arr)
    
    # Check if all elements in the range [A, B] are in the set
    for i in range(A, B + 1):
        if i not in arr_set:
            return False
    return True

# Example Test Cases
print(check_elements([1, 4, 5, 2, 7, 8, 3], 7, 2, 5))  # Output: True
print(check_elements([1, 4, 5, 2, 7, 8, 3], 7, 2, 6))  # Output: False
