class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums[i] for i in range(len(nums)-1) if nums[i] == nums[i+1]]