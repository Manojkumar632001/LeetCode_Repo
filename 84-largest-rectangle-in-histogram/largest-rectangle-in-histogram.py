class Solution(object):
    def largestRectangleArea(self, heights):
        stack=[]
        maxi=0
        for i,h in enumerate(heights):
            ind=i
            while stack and h<stack[-1][1]:
                index,height=stack.pop()
                maxi=max(maxi,height*(i-index))
                ind=index
            stack.append([ind,h])
        for i, h in stack:
            maxi=max(maxi,h*(len(heights)-i))
        return maxi
