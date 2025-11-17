class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
        temp = 10000
        left = 0
        right = 9
        while left <= right:
            mid = (right-left)//2 + left
            if ans[mid] == n:
                return n
            if ans[mid] > n:
                if ans[mid] < temp:
                    temp = ans[mid]
                    right = mid - 1
            else:
                left = mid + 1
        return temp

print(Solution().smallestNumber(100))
