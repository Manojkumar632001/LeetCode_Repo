class Solution:
    def trap(self, height):
        
        maxL=0
        arrL=[0]*len(height)
        arrR=[0]*len(height)
        maxR=0
        for i in range(len(height)):
            j=-i-1
            arrL[i]=maxL
            arrR[j]=maxR
            maxL=max(maxL, height[i])
            maxR=max(maxR, height[j])
        sum=0
        for i in range(len(height)):
            mini=min(arrL[i],arrR[i])
            sum=sum+ max(0,mini-height[i])
        return sum 
        

        

        