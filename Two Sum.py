"""
1. Two Sum
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums, target):
        stack = []
        ans = []
        for i, val in enumerate(nums):
            for j in stack:
                if (val + nums[j] == target):
                    ans.extend([j, i])
                    return ans

            stack.append(i)

    def twoSum2(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i




sol = Solution()
#print ( sol.twoSum([2, 1, 3, 7, 11, 15], 9) )
#print ( sol.twoSum([-3,4,3,90], 0) )
#print ( sol.twoSum2([-3,4,3,90], 0) )
print ( sol.twoSum([3, 3, 1], 4) )
print ( sol.twoSum2([3, 3, 1], 4) )
#print ( sol.twoSum([3, 3], 6) )