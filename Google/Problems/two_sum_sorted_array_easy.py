'''
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        
        # Iterate over the index, value pairs of the array
        for i, value in enumerate(numbers):
            
            # We set the second value that we're looking for to the secondVal var
            secondValue = target - value
            
            # if that value is in the created hashmap
            if secondValue in hashMap:
                
                # Return me the index values (both +1 for a 1 indexed)
                return[hashMap[secondValue] + 1, i + 1]
            # Update the hashmap
            hashMap[value] = i
