class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        res = 0
        i = 0
        while i < (len(s)):
            try:
                temp = "".join([s[i],s[i+1]])
                if temp in romans:
                    res += romans[temp]
                    i += 1
                else:
                    res += romans[s[i]]
            except:
                res += romans[s[i]]
            i += 1
        return res

print(Solution().romanToInt("III"))