class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=b= nums[0]#max sum#current sum
        
        for num in nums[1:]:
            b = max(num, b + num)
            a = max(a, b)
        
        return a
