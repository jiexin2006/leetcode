class Solution:
    def totalMoney(self, n: int) -> int:
        return int(28 * (n//7) + 7* (((n//7 - 1)/2) * (2 + (n//7 - 2))) + ((n%7)/2) * (2*(n//7 + 1) + (n%7 - 1)))

    # full_week = n // 7
    # full_week_savings = 28 * (n//7) + 7* (((n//7 - 1)/2) * (2 + (n//7 - 2)))
    # partial_week = n%7
    # partial_week_savings = ((n%7)/2) * (2*(n//7 + 1) + (n%7 - 1))

print(Solution().totalMoney(20))