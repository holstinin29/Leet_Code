"""
28. Find the Index of the First Occurrence in a String

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i = 0
        while i + len(needle) <= len(haystack):
            if haystack[i:i + len(needle)] == needle:
                return i
            else:
                i += 1

        return -1


haystack = "sadbutsad"
needle = "sad"

sol = Solution()
print ( sol.strStr(haystack, needle) )