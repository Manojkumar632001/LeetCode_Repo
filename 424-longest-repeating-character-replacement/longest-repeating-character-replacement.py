class Solution(object):
    def characterReplacement(self, s, k):
        hashi={}
        maxi=0
        left=0
        for right in range(len(s)):
            hashi[s[right]]=1+hashi.get(s[right],0)
            while (right-left+1)-max(hashi.values())>k:
                hashi[s[left]]=hashi.get(s[left])-1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi
        