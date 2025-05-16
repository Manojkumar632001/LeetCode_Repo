class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total, preSum = 0, 0

        for s in satisfaction:
            if preSum + s > 0:
                preSum += s
                total += preSum
            else:
                break
        return total