"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
class Solution:
    def removeElement(self, nums, val: int) -> int:
        j = 0
        while j < len (nums):
            if nums[j] == val:
                nums.pop(j)
            else:
                j += 1

        print (nums)
        return j


nums = [3,2,2,3,6,8]
val = 3
#nums = [1,1,2]
sol = Solution()
print ( sol.removeElement(nums, val) )