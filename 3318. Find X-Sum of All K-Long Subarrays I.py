class Solution:
    def findXSum(self, nums, k: int, x: int):
        n = len(nums)
        res = []
        for i in range(n-k+1):
            subarray = nums[i:i+k]
            if k == x:
                res.append(sum(subarray))
                continue
            added = []
            occ = dict()
            for num in subarray:
                if num not in added:
                    occ[num]=1
                    added.append(num)
                else:
                    occ[num] += 1
            temp = sorted(occ.items(), key = lambda item: (item[1],item[0]),reverse = True)
            temp2 = 0
            print(temp)
            for j in range(min(x,len(temp))):
                temp2 += temp[j][1]*temp[j][0]
            res.append(temp2)
            print(temp2)
        return res

print(Solution().findXSum([1,4,4,4], k = 3, x = 2))
