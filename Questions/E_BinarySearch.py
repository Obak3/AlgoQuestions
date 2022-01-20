'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Iterate through array
        for i, val in enumerate(nums):
            # If the value at the current index is equal to the target
            if val == target:
                # return the index value
                return i
        # If the solution doesn't exist, return -1
        return -1 

