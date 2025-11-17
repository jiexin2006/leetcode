class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        # k = len(nums)
        # j = 0
        # while j < len(nums):
        #     print(nums)
        #     if nums[j] == val:
        #         nums = nums[:j] + nums[j+1:]
        #         k -= 1
        #         j += 1
        #     else:
        #         j += 1
        #         continue
        # if nums[j] == val:
        #     nums.pop(j)
        # return k

        # k = len(nums)
        # length = len(nums)
        # for i in range(length):
        #     print(length)
        #     if nums[i] == val:
        #         nums.pop(i)
        #         k-=1
        # nums = sorted(nums)
        # print(nums)
        # return k

        # k = len(nums)
        # res = [0 for i in range(len(nums))]
        # i = 0
        # for j in range(len(nums)):
        #     print(res)
        #     if nums[j] == val:
        #         k -= 1
        #     else:
        #         res[i] = nums[j]
        #         i += 1
        # nums = res
        # print(nums)
        # return k

print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))