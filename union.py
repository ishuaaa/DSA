class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        c= a+b
        c.sort()
        d=[]
        for i in range(len(c)):
            if i==0 or c[i]!=c[i-1]:
                d.append(c[i])
        return d
                