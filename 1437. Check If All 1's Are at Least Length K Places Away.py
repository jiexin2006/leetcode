class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        if k == 0:
            return True
        j = None
        for i in range(len(nums)):
            # print(one, j)
            if nums[i] == 1:
                if j is not None and i - j - 1 < k:
                    return False
                else:
                    j = i
        return True

print(Solution().kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
