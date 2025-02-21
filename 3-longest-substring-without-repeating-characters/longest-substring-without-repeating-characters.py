class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        maxi=0
        se=set()
        for right in range(len(s)):
            while s[right] in se:
                se.remove(s[left])
                left+=1
            se.add(s[right])
            maxi=max(maxi,right-left+1)
            right=right+1
        return maxi



        