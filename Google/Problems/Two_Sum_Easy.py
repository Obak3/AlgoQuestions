'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        secondValue = 0
        
        for i in range(len(nums)):
            if target - i in nums:
                secondValue = target - i
                ans.append(nums.index(secondValue))
                ans.append(nums.index(i))

        # Return the index values of nums that add up to the target
        return ans
