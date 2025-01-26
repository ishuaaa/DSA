class Solution:
    def getSecondLargest(self, arr):
        
         if len(arr)<2:
             return -1
         large= secondlarge =-1
         for i in range(len(arr)):
            if arr[i]>large:
                secondlarge=large
                large=arr[i]
            elif arr[i]>secondlarge and arr[i]!=large:
                secondlarge=arr[i]
         return secondlarge
        