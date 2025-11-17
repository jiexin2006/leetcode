class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        if colors == "":
            return 0
        res = 0
        i = 1
        while i < len(colors):
            if colors[i-1] == colors[i]:
                j = i-1
                temp = []
                while j < len(colors) and colors[j] == colors[i]:
                    temp.append(neededTime[j])
                    #print(temp)
                    j+=1
                temp = sorted(temp)
                #print("sorted", temp, "-1", temp[:-1])
                res += sum(temp[:-1])
                i = j + 1
            else:
                i += 1

        return res

print(Solution().minCost(colors = "bbbaaa", neededTime = [4,9,3,8,8,9]))


# def minCost(self, colors: str, neededTime: List[int]) -> int:
#     cost = 0;
#     i = 0
#     while i < len(colors) - 1:
#         maxcost = neededTime[i]
#         while i < len(colors) - 1 and colors[i] == colors[i + 1]:
#             cost += min(maxcost, neededTime[i + 1])
#             maxcost = max(maxcost, neededTime[i + 1])
#             i += 1
#         i += 1
#     return cost