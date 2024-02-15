"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


"""


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            m = (low + high) // 2
            guess = nums[m]
            if (target < guess):
                high = m - 1
            elif (target > guess):
                low = m + 1
            else:
                return m

        if (target > guess):
            return m + 1
        else:
            return m



nums = [1,3,5,6]
target = 7

nums = [1,3]
target = 2


sol = Solution()
print ( sol.searchInsert(nums, target) )