class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Edge case: empty array
    
        k = 1  # First element is always unique
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # If a new unique element is found
                nums[k] = nums[i]  # Move it to the correct position
                k += 1  # Increment unique count
        return k

        