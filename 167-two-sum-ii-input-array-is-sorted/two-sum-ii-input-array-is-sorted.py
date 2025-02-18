class Solution(object):
    def twoSum(self, numbers, target):
        right,left=0,len(numbers)-1
        while (left>right):
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [right+1, left+1]
            elif target>sum:
                right=right+1
            elif target<sum:
                left=left-1



        