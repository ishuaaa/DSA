class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        self.arr=arr
        for i in range(0, len(arr)):
            swapped=False
            for j in range(0,len(arr)-i-1):
                 if arr[j+1]<arr[j]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            if swapped==False:
                break
            