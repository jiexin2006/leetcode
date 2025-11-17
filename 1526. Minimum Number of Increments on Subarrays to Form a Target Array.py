class Solution:
    def minNumberOperations(self, target) -> int:
        res = target[0]
        for i in range(1,len(target)):
            if target[i] > target[i-1]:
                res += target[i] - target[i -1]
        return res

print(Solution().minNumberOperations([3,1,5,4,2]))