class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        
        for i, val in enumerate(nums): 
            if val in counts:
                counts[val] += 1
            else: 
                counts[val] = 1
                
        for i, val in counts.items():
            if val == 1:
                return i
