"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        curr = dummy = ListNode ()

        while list1 is not None or list2 is not None:

            val_1 = list1.val if list1 else float ('inf')
            val_2 = list2.val if list2 else float ('inf')

            if val_1 < val_2:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        return dummy.next





list1_1 = ListNode(1)
list1_2 = ListNode(2)
list1_3 = ListNode(3)
list1_4 = ListNode(4)

list1_1.next = list1_2
list1_2.next = list1_3
list1_3.next = list1_4

###########################

list2_1 = ListNode(1)
list2_2 = ListNode(2)
list2_3 = ListNode(3)

list2_1.next = list2_2
list2_2.next = list2_3


sol = Solution()
res = sol.mergeTwoLists(list1_1, list2_1)

while (res):
    print (res.val)
    res = res.next
