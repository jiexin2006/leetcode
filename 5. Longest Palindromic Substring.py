class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1 or len(s) ==0:
            return s
        palindrome = s[0]
        i = 0
        while i <= len(s)-3:
            temp = s[i:i+3]
            print("checking:", temp)
            if temp[0]==temp[2]:
                j = i
                k = i + 2
                while j-1 >=0 and k+1 < len(s) and s[j-1]==s[k+1]:
                    j-=1
                    k+=1
                    print("j =",j, "k=",k)
                if k+1-j > len(palindrome):
                    palindrome = s[j:k+1]
            i += 1
            print("current palindrome: ",palindrome)
        i = 0
        while i <=len(s)-2:
            temp = s[i:i+2]
            print("checking:", temp)
            if temp[0]==temp[1]:
                j = i
                k = i + 1
                while j-1 >=0 and k+1 < len(s) and s[j-1]==s[k+1]:
                    j-=1
                    k+=1
                if k+1-j > len(palindrome) and j >=0:
                    palindrome = s[j:k+1]
            i += 1
            print("current palindrome: ",palindrome)

        return palindrome

print(Solution().longestPalindrome("adam"))