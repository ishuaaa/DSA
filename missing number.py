class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=len(nums)
        for i in range(a):
            if i not in nums:
                return i
        else:
            return a