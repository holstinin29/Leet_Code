"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def isPalindrome(s):
    new_s = ''
    for elem in s:
        if elem.isalnum():
            new_s += elem.lower()

    return new_s == new_s[::-1]

s = "A man, a plan, a canal: Panama"
print (isPalindrome (s) )