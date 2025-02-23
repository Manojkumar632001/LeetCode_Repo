class Solution(object):
    def dailyTemperatures(self, temp):
        stack=[]
        res=[0]*len(temp)
        for i,t in enumerate(temp):
            while stack and t>stack[-1][1]:
                stackI,stackT=stack.pop()
                res[stackI]=i-stackI
            stack.append([i,t])
        return res
        