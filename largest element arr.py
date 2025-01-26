from typing import List


class Solution:
    def largest(self, arr):
        a=len(arr)
        b=arr[0]
        for i in range(1,a):
            if arr[i]>b:
                b=arr[i]
        return b