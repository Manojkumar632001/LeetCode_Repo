class Solution(object):
    def maxProfit(self, price):
        right=1
        left=0
        maxi=0
        while right<len(price):
            if price[right]>price[left]:
                maxi=max(price[right]-price[left],maxi)
            else:
                left=right
            right=right+1
        return maxi

        