"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len (a) - 1
        j = len (b) - 1
        dop = 0
        res = ""

        while i >= 0 or j >= 0:

            val_a = 0 if i < 0 else int(a[i])
            val_b = 0 if j < 0 else int(b[j])
            result = val_a + val_b + dop

            dop = 1 if result > 1 else 0
            
            res = str(result % 2) + res

            i -= 1
            j -= 1

        if (dop > 0):
            res = str(dop % 2) + res

        return (res)









a = "1010"
b = "1011"


sol = Solution()
print(sol.addBinary(a, b))