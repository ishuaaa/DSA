class Solution:
    def insertionSort(self, arr):
        self.arr=arr
        for i in range(len(arr)):
            for j in range(0,i):
                if arr[i]<arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]