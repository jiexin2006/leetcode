class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        next_zero = [n for _ in range(n)]
        for i in range(n-2, -1, -1):
            if s[i + 1] == "0":
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i + 1]
        # print(next_zero)
        res = 0
        for l in range(n):
            r = l
            zeroes = 1 if s[l] == "0" else 0
            while zeroes * zeroes <= n:
                next_z = next_zero[r]
                ones = (next_z - l) - zeroes
                if ones >= zeroes * zeroes:
                    res += min(next_z - r, ones - zeroes*zeroes + 1)
                r = next_z
                zeroes += 1
                if r == n:
                    break
        return res

print(Solution().numberOfSubstrings("00011"))