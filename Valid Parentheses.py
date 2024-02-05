"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
class Solution:
    def isValid(self, s: str) -> bool:

        cnt_open_a = 0
        cnt_open_b = 0
        cnt_open_c = 0

        cnt_closed_a = 0
        cnt_closed_b = 0
        cnt_closed_c = 0

        set_open = ('(', '[', '{')
        set_closed = (')', ']', '}')

        list_expected = []

        for char in s:
            if char in set_open:

                if char == set_open[0]:
                    cnt_open_a += 1
                    list_expected.insert(0, set_closed[0])

                if char == set_open[1]:
                    cnt_open_b += 1
                    list_expected.insert(0, set_closed[1])

                if char == set_open[2]:
                    cnt_open_c += 1
                    list_expected.insert(0, set_closed[2])


            elif char in set_closed and len (list_expected) > 0:
                if char == list_expected[0]:
                    if char == set_closed[0]:
                        cnt_closed_a += 1

                    if char == set_closed[1]:
                        cnt_closed_b += 1

                    if char == set_closed[2]:
                        cnt_closed_c += 1

                    list_expected.pop(0)
                else:
                    return False

            else:
                return False

        if cnt_closed_a != cnt_open_a or cnt_closed_b != cnt_open_b or cnt_closed_c != cnt_open_c:
            return False
        else:
            return True





s = "()[]{}"
s = "([)]"
s = "]"
sol = Solution()
print ( sol.isValid(s) )