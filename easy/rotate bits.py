"""Given an integer N and an integer D, rotate the binary representation of the integer N by D digits to the left as well as right and return the results in their decimal representation after each of the rotation.
Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000000000001100. Output array should follow {leftrotation, rightrotation}.

Examples :

Input: n = 28, d = 2
Output: [112, 7]
Explanation: 28 in Binary is: 0000000000011100. Rotating left by 2 positions, it becomes 0000000001110000 = 112 (in decimal). Rotating right by 2 positions, it becomes 0000000000000111 = 7 (in decimal).

Input: n = 29, d = 2
Output: [116, 16391]
Explanation: 29 in Binary is: 0000000000011101. Rotating left by 2 positions, it becomes 0000000001110100 = 116 (in decimal). Rotating right by 2 positions, it becomes 010000000000111 = 16391 (in decimal).

Input: n = 11, d = 10
Output: [11264, 704]"""


class Solution:
    def rotate(self, N, D):
        D = D % 16  # Reduce D to avoid unnecessary full rotations
        
        # Left Rotate
        left_rot = ((N << D) | (N >> (16 - D))) & 0xFFFF  # Mask to keep 16 bits
        
        # Right Rotate
        right_rot = ((N >> D) | (N << (16 - D))) & 0xFFFF  # Mask to keep 16 bits
        
        return [left_rot, right_rot]

# Test cases
sol = Solution()
print(sol.rotate(28, 2))   # Output: [112, 7]
print(sol.rotate(29, 2))   # Output: [116, 16391]
print(sol.rotate(11, 10))  # Output: [11264, 704]
