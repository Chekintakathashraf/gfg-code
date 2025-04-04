'''As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar that contains N chocolate squares. Each of the squares has a tastiness level which is denoted by an array A[].
Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first. 
Determine the tastiness level of the square which his sister gets.

Example 1:

Input : arr[ ] = {5, 3, 1, 6, 9}
Output : 1
Explanation:
Initially: 5 3 1 6 9
In first step: 5 3 1 6
In Second step: 5 3 1
In Third step: 3 1
In Fourth step: 1
Return 1



Example 2:

Input : arr[ ] = {5, 9, 2, 6} 
Output :  2

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function chocolates() that takes an array (arr), sizeOfArray (n) and return the tastiness level of the square which his sister gets. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).'''

def chocolates(arr, n):
    left = 0
    right = n - 1
    
    # Simulate the game until only one square is left
    while left < right:
        if arr[left] > arr[right]:
            left += 1  # Ishaan picks the left square
        else:
            right -= 1  # Ishaan picks the right square
    
    # The last square left will be the sister's square
    return arr[left]

# Test cases
print(chocolates([5, 3, 1, 6, 9], 5))  # Output: 1
print(chocolates([5, 9, 2, 6], 4))     # Output: 2
