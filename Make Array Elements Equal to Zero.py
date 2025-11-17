class Solution:
    # ®def move(self,nums, direction, curr):
    #     while nums.count(0) != len(nums):
    #         if nums[curr] < 0:
    #             return 0
    #         if nums[curr] != 0:
    #             nums[curr] -= 1
    #             direction = -direction
    #         curr += direction
    #         if curr < 0 or curr > len(nums)-1:
    #             return 0
    #     return 1
    #
    # def countValidSelections(self, nums) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             continue
    #         else:
    #             temp = nums.copy()
    #             res += self.move(temp, -1, i)
    #             res += self.move(temp, 1, i)
    #     return res

    def countValidSelections(self, nums) -> int:
        res = 0
        sums = [0 for i in range(len(nums))]
        sums[0] = nums[0]
        for i in range(1,len(nums)):
            sums[i] = nums[i] + sums[i-1]
        print(sums)
        for j in range(len(nums)):
            if nums[j] != 0:
                continue
            else:
                if abs(sums[j] - (sums[-1]-sums[j]))==0:
                    res += 2

                elif abs(sums[j] - (sums[-1]-sums[j]))==1:
                    res += 1
                else:
                    continue
        return res

print(Solution().countValidSelections([1,0,2,0,3]))
