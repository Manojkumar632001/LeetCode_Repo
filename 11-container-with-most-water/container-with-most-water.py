class Solution(object):
    def maxArea(self, heights):
    
        s=0
        right,left=len(heights)-1,0
        while left<right:
            
            mini=min(heights[left],heights[right])
            s=max(s,mini*(right-left))
            
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return s

        