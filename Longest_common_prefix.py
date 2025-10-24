class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = strs[0]
        for i in range(1, len(strs)):
            if len(res) == 0:
                return ""
            x = min(len(strs[i]), len(res))
            res = res[:x]
            for j in range(x):
                if res[j] != strs[i][j]:
                    res = res[:j]
                    break

        return res

print(Solution().longestCommonPrefix(["flower","flow","flight"]))

# most efficient solution:
# minLen = len(strs[0])
# for i in range(1, len(strs)):
#     if (len(strs[i]) < minLen):
#         minLen = len(strs[i])
#
# index = -1
# L = 0
# R = minLen
# while L < R:
#     mid = L + ((R - L) // 2)    Binary search!
#     found = True
#     for i in range(1, len(strs)):
#         if (strs[0][:mid + 1] != strs[i][:mid + 1]):
#             found = False
#             break
#     if (found):
#         index = mid
#         L = mid + 1
#     else:
#         R = mid
#
# return strs[0][:index + 1]