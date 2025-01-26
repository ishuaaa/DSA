class Solution:
    def check(self, nums: List[int]) -> bool:
         for i in range(1,len(nums)):
             if nums[i]>=nums[i-1] and nums[i]<=nums[i+1]:
                return True
             else:
                return False