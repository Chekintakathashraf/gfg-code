def reverse_string(s):
    i = 0
    j = len(s) - 1
    
    while i < j:                    # Step 3: Loop until pointers meet or cross
        s[i], s[j] = s[j], s[i]     # Step 4: Swap elements at i and j
        i += 1                      # Step 5: Move left pointer forward (i + 1)
        j -= 1                      # Step 6: Move right pointer backward (j - 1)

s = ["p", "y", "t", "h", "o", "n"]
reverse_string(s)
print(s)

