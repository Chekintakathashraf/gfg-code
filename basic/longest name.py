"""Given an array arr[] containing strings of names. Your task is to return the longest string. If there are multiple names of the longest size, return the first occurring name.

Examples :

Input: arr[] = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
Output: "GeeksforGeeks"
Explanation: name "GeeksforGeeks" has maximum length among all names. 

Input: arr[] = ["Apple", "Mango", "Orange", "Banana"]
Output: "Orange"
Explanation: names "Orange" and "Banana" both have maximum length among all names but Orange comes first so answer will be "Orange". """


class Solution:
    def longestString(self, arr):
        max_str = arr[0]  # Assume the first string is the longest
        
        for s in arr:
            if len(s) > len(max_str):
                max_str = s  # Update longest string
        
        return max_str

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.longestString(["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]))  # Output: "GeeksforGeeks"
    print(solution.longestString(["Apple", "Mango", "Orange", "Banana"]))  # Output: "Orange"

