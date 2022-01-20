'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a solutions hashmap
        base_hashmap = {}
        # Iterate through the array
        for i, val in enumerate(nums):
            complement = target - val
            # Check if the complement to the target is in the map
            if complement in base_hashmap:
                # Return an array of the two index values
                return [base_hashmap[complement], i]
            base_hashmap[val] = i
