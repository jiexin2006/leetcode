class Solution:
    def removeDuplicates(self, nums) -> int:
        if nums:
            k = 1
        else:
            return 0
        temp = nums.copy()
        for i in range(1,len(temp)):
            if temp[i] != temp[i-1]:
                nums[k] = temp[i]
                k += 1
        return k

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
