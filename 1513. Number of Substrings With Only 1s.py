class Solution:
    def numSub(self, s: str) -> int:
        curr = -1
        res = 0
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != "0":
                i += 1
            # print(i, curr)
            # print("Checking: ", s[i:curr + 1])
            ones = i - curr - 1
            ones = ones * (ones + 1)
            res = (ones//2) % (10**9 + 7)
            curr = i
            i += 1
        return res

        # next_zero = [n for _ in range(n)]
        # for i in range(n-2, -1, -1):
        #     if s[i+1] == "0":
        #         next_zero[i] = i + 1
        #     else:
        #         next_zero[i] = next_zero[i + 1]
        # res = 0
        # next_z = 0
        # for i in range(n):



print(Solution().numSub("111111"))