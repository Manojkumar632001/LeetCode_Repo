class Solution(object):
    def reverseWords(self, s):
        r=s.strip().split()
        r=r[::-1]
        s= " ".join(r)
        return s
        
        
        