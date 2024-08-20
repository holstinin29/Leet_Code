"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


class Solution:
    def singleNumber(self, nums):
        seen = []
        for i in range (len(nums) ):
            if nums[i] not in nums[i+1:] and nums[i] not in seen:
                return nums[i]
            else:
                seen.append(nums[i])
        return nums[i]




nums = [2,2,1]
sol = Solution()
print(sol.singleNumber(nums))