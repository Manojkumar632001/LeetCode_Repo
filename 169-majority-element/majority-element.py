class Solution(object):
    def majorityElement(self, nums):
        res = None
        count = 0
        for i in nums:
            if count == 0:
                res = i
                count += 1
            elif res == i:
                count += 1
            else:
                count -= 1
        return res  # Return the result after the loop finishes
