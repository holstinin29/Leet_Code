"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    for i in range(len(s)):
        if s[i] not in t:
            return False
        else:
            t = t[:t.index(s[i])] + t[t.index(s[i]) + 1:]
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))