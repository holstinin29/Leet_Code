"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

"""

def reverseVowels(s):

    l, r = 0, len(s)-1
    list_s = list(s)

    list_lettera = ['A', 'E', 'U', 'I', 'O']

    while r > l:
        if list_s[l].upper() in list_lettera and list_s[r].upper() in list_lettera:
            list_s[l], list_s[r] = list_s[r], list_s[l]

            l += 1
            r -= 1

        else:
            if list_s[l].upper() in list_lettera:
                r -= 1
            else:
                l += 1

    return ''.join(list_s)

s = "IceCreAm"
#s = "ba"
#s = "ab"
s = "vmg"
print (reverseVowels(s))