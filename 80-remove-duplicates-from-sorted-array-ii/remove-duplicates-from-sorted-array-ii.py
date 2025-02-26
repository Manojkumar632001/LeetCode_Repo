class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        index = 2  # Start from the third element
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:  # Check if it can be added
                nums[index] = nums[i]
                index += 1

        return index