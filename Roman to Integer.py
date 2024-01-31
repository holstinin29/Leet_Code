class Solution:
    def romanToInt(self, s: str) -> int:

        dict_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sum = 0

        for i in range( len(s)):
            sum += dict_numbers[s[i]]
            if dict_numbers[s[i]] > dict_numbers[s[i-1]] and i > 0:
                 sum += - dict_numbers[s[i-1]] * 2

        print (sum)
        return (sum)

s = Solution()
s.romanToInt(input())