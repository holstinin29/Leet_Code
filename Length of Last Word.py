"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring  consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i, char in enumerate(s):
            if char != ' ' and ( i == 0 or s[i-1 ] == ' '):
                len_word = 1
            elif char != ' ':
                len_word += 1

        return len_word



s = "   fly me   to   the moon  "
sol = Solution()
print ( sol.lengthOfLastWord(s) )