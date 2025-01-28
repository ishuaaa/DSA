class Solution:
    def longestSubarray(self, arr, k): 
        prefix_sum=0
        prefix_map={0:-1}
        length=0
        for i,nums in enumerate(arr):
            prefix_sum+=nums
            if prefix_sum-k in prefix_map:
                length=max(length,i-prefix_map[prefix_sum-k])
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum]=i
        return length        
            