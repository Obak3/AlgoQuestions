class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	nums = [2,7,11,15]
	
	for i in range(len(nums)): 
		validSum = target - nums[i]
		nums = nums[i:]
		
		if validSum in nums:
			return (i, nums.index(validSum))
