class Solution:
 
    def mergeSort(self,arr, l, r):
           if l < r: 
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)
    def merge(self, arr, l, mid, r):
       
        a = arr[l:mid + 1]
        b = arr[mid + 1:r + 1]
        i = 0  
        j = 0
        k = l
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1