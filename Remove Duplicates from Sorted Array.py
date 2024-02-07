"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums) -> int:

        #for i, el in enumerate(nums, 0):
        #for el in nums[1:]:
        i = 0
        while i < len (nums):

           if i == len (nums) - 1 or nums[i] < nums[i + 1]:
                i += 1
           else:
                nums.pop(i)

        print (nums)

        return i




nums = [0,0,1,1,1,2,2,3,3,4,5]
#nums = [1,1,2]
sol = Solution()
print ( sol.removeDuplicates(nums) )