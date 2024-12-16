"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    for i in range (len(s)):
        s.insert(i, s.pop())

    #s = s[::-1]
    return (s)


s = ["H","a","n","n","a","h"]
s = ["a","b","c","d"]
print (reverseString(s))
