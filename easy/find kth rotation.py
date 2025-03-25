"""Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Examples:

Input: arr = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.

Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.

Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)"""

def find_rotation_count(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        # If array is already sorted, return 0 (not rotated)
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2
        next_idx = (mid + 1) % len(arr)
        prev_idx = (mid - 1 + len(arr)) % len(arr)

        # Check if mid element is the minimum
        if arr[mid] <= arr[prev_idx] and arr[mid] <= arr[next_idx]:
            return mid  # The number of rotations

        # Decide which half to search
        if arr[mid] >= arr[low]:  # Left half is sorted, go right
            low = mid + 1
        else:  # Right half is sorted, go left
            high = mid - 1

    return 0  # Edge case: If no rotation detected (sorted array)

# Test cases
print(find_rotation_count([5, 1, 2, 3, 4]))  # Output: 1
print(find_rotation_count([1, 2, 3, 4, 5]))  # Output: 0
print(find_rotation_count([3, 4, 5, 1, 2]))  # Output: 3
print(find_rotation_count([6, 9, 12, 15, 18, 2, 3]))  # Output: 5
