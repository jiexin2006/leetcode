class Solution:
    def getSneakyNumbers(self, nums):
        nums = sorted(nums)
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
        return res

print(Solution().getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))