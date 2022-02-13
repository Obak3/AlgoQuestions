'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# OR

    def containsDuplicate(self, nums: List[int]) -> bool:
        tracking = {}

        for i in nums:
            if i in tracking:
                return True
            else:
                tracking[i] = nums.index(i)

        return False

