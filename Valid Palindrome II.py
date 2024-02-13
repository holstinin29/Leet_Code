"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        cnt_error = 0
        max_cnt_error = 2

        while i < j:
            if s[i] != s[j]:
                cnt_error += 1

                l = i + 1
                k = j
                cnt_coincidence_l = 0
                while l < k and True:
                    if s[l] != s[k]:
                        False
                    else:
                        cnt_coincidence_l += 1

                    l += 1
                    k -= 1

                l = i
                k = j - 1
                cnt_coincidence_r = 0
                while l < k and True:
                    if s[l] != s[k]:
                        False
                    else:
                        cnt_coincidence_r += 1

                    l += 1
                    k -= 1


                if cnt_coincidence_l > cnt_coincidence_r:
                    j += 1
                else:
                    i -= 1


                if (cnt_error > 1):
                    return False
            i += 1
            j -= 1
        return True



s = "abac"

sol = Solution()
print ( sol.validPalindrome(s) )