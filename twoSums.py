class Solution:
    def twoSum(self, nums, target):
        # nums_copy = {nums[i]: i for i in range(len(nums))}
        # print(nums_copy)
        # nums = sorted(nums)
        # left_pointer = 0
        # right_pointer = len(nums_copy) - 1
        # while True:
        #     check = nums[left_pointer] + nums[right_pointer]
        #     if check == target:
        #         return [nums_copy[nums[left_pointer]], nums_copy[nums[right_pointer]]]
        #     if check > target:
        #         right_pointer -= 1
        #         continue
        #     if check < target:
        #         left_pointer += 1
        #         continue

        nums_copy = [(nums[i], i) for i in range(len(nums))]
        nums_copy = sorted(nums_copy)
        left_pointer = 0
        right_pointer = len(nums_copy) - 1
        while True:
            check = nums_copy[left_pointer][0] + nums_copy[right_pointer][0]
            if check == target:
                return [nums_copy[left_pointer][1], nums_copy[right_pointer][1]]
            if check > target:
                right_pointer -= 1
                continue
            if check < target:
                left_pointer += 1
                continue


print(Solution().twoSum([3,3], 6))