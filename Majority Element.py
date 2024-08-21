"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
def majorityElement(nums):
    seen = {}
    last_cnt_maj = 0
    for elem in nums:
        now_cnt_maj = seen.get(elem, 0)
        now_cnt_maj += 1
        if now_cnt_maj >= last_cnt_maj:
            last_cnt_maj = now_cnt_maj
            maj_elem = elem
        seen[elem] = now_cnt_maj

    return maj_elem


nums = [2,2,1,1,1,2,2]
nums =[3,3,4]
nums = [8,8,7,7,7]
print (majorityElement(nums))