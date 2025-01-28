class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        max1=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                max1=max(max1,c)
            else:
                c=0
        return max1