class Solution(object):
    def isValid(self, s):
        hashi={']':'[',
                '}':'{',
                ')':'('}
        stack=[]
        for i in s:
            if i not in hashi:
                stack.append(i)

            elif stack and stack[-1]==hashi[i]:
                stack.pop()

            else:
                return False
        if stack==[]:
            return True
        else:
            return False
