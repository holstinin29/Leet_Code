"""
9. Palindrome Number

Given an integer x, return true if x is a
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        i = 0
        rank = 0
        while x >= 10 ** i:
            rank = 10 ** i
            i += 1

        while x:
            left = x // rank
            right = x % 10

            if left != right: return False

            #x = (x % rank) // 10
            x -= left * rank
            x //= 10

            rank /= 100

        return True



x = 121
sol = Solution()
print ( sol.isPalindrome(x) )