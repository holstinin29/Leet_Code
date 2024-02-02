"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:

        first_word = strs[0]
        prefix = ''

        i = 0
        while True:

            for word in strs[0:]:
                if (i >= len(word)):
                    return prefix

                elif first_word[i] != word[i]:
                    return prefix

            prefix += word[i]

            i += 1

        return prefix

a = Solution()
l = ["flower","flow","flight"]
prefix = a.longestCommonPrefix(l)
print (prefix)