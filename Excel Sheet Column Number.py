"""
171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
"""
import string
def titleToNumber(columnTitle):
    d = {string.ascii_uppercase[i]: i+1 for i in range (len(string.ascii_uppercase)) }

    sum = 0
    for elem in columnTitle:
        sum = sum * 26 +  d[elem]

    return sum


columnTitle = 'ZY'
columnTitle = "FXSHRXW"
columnTitle = "ABC"
print (titleToNumber(columnTitle))