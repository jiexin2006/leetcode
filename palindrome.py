class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstring = str(x)
        left_pointer = 0
        right_pointer = len(xstring) - 1
        while True:
            if xstring[left_pointer] != xstring[right_pointer]:
                return False
            elif left_pointer == right_pointer or right_pointer-left_pointer == 1:
                return True
            else:
                left_pointer += 1
                right_pointer -= 1