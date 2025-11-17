class Solution:
    def numberOfBeams(self, bank) -> int:
        row = []
        for r in bank:
            temp = 0
            for i in r:
                if i == "1":
                    temp += 1
            if temp == 0:
                continue
            else:
                row.append(temp)

        return sum([row[i] * row[i + 1] for i in range(len(row)-1)])

print(Solution().numberOfBeams(["000","111","000"]))
